# testWork

    Здесь вкратце дается обзор предлагаемого решения по тестовому заданию https://shiftproject.ru/resources/uploads/SHIFT_Java_Test_Task_f8f56f0c1e.pdf

   Пользовался версией java 25.0.2 2026-01-20 LTS, взятой на сайте 
https://www.oracle.com/asean/java/technologies/downloads/. Одной из фич данной версии 
является возможность запускать исходник на исполнение в командной строке:

    java Program.java

без использования редакторов типа NetBeans и явного запуска компиляторов
типа javac и использования систем сборок типа Maven. Если запустить нашу 
программу filter.java без аргументов, то на экран выведется:

Error in arguments. Usage: java filter.java <arguments>

Where <arguments> is one or few of:

         -o <path_to_folder> to use folder for output files
         
         -p <prefix> to use prefix for output filenames
         
         -[s|f] to display small or full statistic
         
         -a to use append Mode for output files
         
         <files> to use list of input files
         
By example: java filter.java -o subfolder in1.txt in2.txt

В данной репозитории прилагается исходник filter.java по решению поставленной задачи, а также
сопуствующие служебные файлы. Спасибо за интерес к данной работе.
