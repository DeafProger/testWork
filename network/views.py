from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.pagination import PageNumberPagination
from network.models import Supplier, Contact, Product
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


class SupplierPaginator(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class SupplierCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('company_name', 'level', 'supplier_name', 'debt',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'launched_at', 'supplier',)


class IsOwner(BasePermission):
    message = 'You is not page Owner.'
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsProductOwner(BasePermission):
    message = 'You is not page Owner.'
    def has_object_permission(self, request, view, obj):
        return request.user == obj.supplier.owner


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'country', 'city', 'street', 'house_number',)


class SupplierSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(source='contacts')
    product_list = ProductSerializer(
        source='product_set',
        many=True,
        read_only=True
    )

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contacts', None)
        if contact_data:
            contact_serializer = ContactSerializer(
                instance=instance.contacts,
                data=contact_data
            )

            if contact_serializer.is_valid():
                contact_serializer.save()

        return instance

    class Meta:
        model = Supplier
        fields = (
            'company_name', 'level', 'supplier_name',
            'debt', 'created_at', 'product_list', 'contact',
        )
        read_only_fields = ('debt', 'created_at',)


class IsContactCreator(BasePermission):
    message = 'You is not contacts Creator.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator


class IsSuperUser(BasePermission):
    message = 'You is not super User.'

    def has_permission(self, request, view):
        return request.user.is_superuser


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    default_serializer = SupplierSerializer
    pagination_class = SupplierPaginator
    serializers = {
        'create': SupplierCreateSerializer,
    }

    def perform_create(self, serializer):
        new_link = serializer.save()
        new_link.owner = self.request.user
        new_link.save()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        match self.action:
            case 'create' | 'list':
                permission_classes = [IsAuthenticated]
            case _:
                permission_classes = [IsAuthenticated, IsOwner | IsSuperUser]

        return [permission() for permission in permission_classes]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        match self.action:
            case 'create' | 'list':
                permission_classes = [IsAuthenticated]
            case _:
                permission_classes = [
                    IsAuthenticated, IsProductOwner | IsSuperUser
                ]
        return [permission() for permission in permission_classes]


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        new_contact = serializer.save()
        new_contact.creator = self.request.user
        new_contact.save()

    def get_permissions(self):
        match self.action:
            case 'create' | 'list':
                permission_classes = [IsAuthenticated]
            case _:
                permission_classes = [
                    IsAuthenticated, IsContactCreator | IsSuperUser
                ]

        return [permission() for permission in permission_classes]
