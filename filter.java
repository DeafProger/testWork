import static java.lang.System.*;
import java.io.*;

public class filter {

    public static void writeResults(String strings, String filename, boolean append) {
        out.println("write to file " + filename + " ...");
        try(BufferedWriter bw = new BufferedWriter(new FileWriter(filename, append))) {
            bw.write(strings);
        } catch(IOException ex) {
            out.println(ex.getMessage());
            exit(-3);
        } 
    }

    public static boolean isNumeric(String line) {
        try {
            Double.parseDouble(line);
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }

    public static boolean isInteger(String line) {
        // после фильтрации в функции isNumeric line содержит только числовое данное
        if (line.indexOf(".") != -1) return false;
        String Line = line.toLowerCase();
        if (Line.indexOf("f") != -1) return false;
        if (Line.indexOf("e") != -1) return false;
        return true;
    }

    public static void errMsg() {
        out.println("Error in arguments. Usage: java filter.java <arguments>");
        out.println("Where <arguments> is one or few of:");
        out.println("\t -o <path_to_folder> to use folder for output files ");
        out.println("\t -p <prefix> to use prefix for output filenames");    
        out.println("\t -[s|f] to display small or full statistic");
        out.println("\t -a to use append Mode for output files");
        out.println("\t <files> to use list of input files");
        out.println("By example: java filter.java -o subfolder in1.txt in2.txt");
        exit(-1);
    }
    
    public static void main(String[] args) {
        
        String intName = "integers.txt";
        String strName = "strings.txt";
        String fltName = "floats.txt";
        String integers = ""; // for accumulate info and writing to "integers.txt"
        String strings = "";  // for accumulate info and writing to "strings.txt"
        String floats = "";   // for accumulate info and writing to "floats.txt"

        String filenames = "";  // list of inputfilenames, separated by 0x00 
                                // in java 0x00 is not end of string
        boolean append = false; // for check append mode
        boolean full = false;   // for check full statistic mode
        String prefix = "";
        String path = "";

        if (args.length > 0) {

            for (int i = 0; i < args.length;) {
                switch (args[i]) {
                    case "-p" -> { 
                        if (++i < args.length) prefix = args[i];
                            else errMsg();
                    }
                    case "-o" -> { 
                        if (++i < args.length) path = args[i];
                            else errMsg();
                    }
                    case "-a" -> append = true; 
                    case "-s" -> full = false; 
                    case "-f" -> full = true; 
                    default -> filenames += args[i] + "\0";
                }
                i++;
            }

        } else errMsg();

        String[] files = filenames.split("\0");
        filenames = "";  

        for (String file : files) {
            out.println("accumulate info from file " + file + " ...");    
            try(BufferedReader br = new BufferedReader(new FileReader(file))) {
                String line = "";
                while((line = br.readLine()) != null){
                    if (isNumeric(line)) {
                        if (isInteger(line)) integers += line + "\n";
                            else floats += line + "\n";
                    } else strings += line + "\n";
                }
            }
            catch(IOException ex) {
                out.println(ex.getMessage());
                exit(-2);
            } 
        } 

        if (path != "") {
            char last = path.charAt(path.length() - 1);
            if (last != '/' && last != '\\') path += "/";
        }

        int ilen = 0, slen = 0, flen = 0;

        String[] ints = integers.split("\n");
        String[] strs = strings.split("\n");
        String[] flts = floats.split("\n");
        
        if (ints.length > 0 && ints[0].length() > 0) ilen = ints.length;
        if (strs.length > 0 && strs[0].length() > 0) slen = strs.length;
        if (flts.length > 0 && flts[0].length() > 0) flen = flts.length;

        if (ilen > 0) writeResults(integers, path + prefix + intName, append);
        if (slen > 0) writeResults(strings, path + prefix + strName, append);   
        if (flen > 0) writeResults(floats, path + prefix + fltName, append);     

        out.print("integers: " + ilen + ", ");
        out.print("strings: " + slen + ", ");
        out.println("floats: " + flen);

        if (full){
            if (ilen + flen > 0) {
                Double max, min, sum, avg; 
                if (ilen > 0) max = Double.parseDouble(ints[0]);
                    else max = Double.parseDouble(flts[0]);    
                min = max;
                sum = 0.0;

                if (ilen > 0) {
                    for (String item : ints){
                        Double cur = Double.parseDouble(item);
                        if (max < cur) max = cur;
                        if (min > cur) min = cur;
                        sum += cur; 
                    }
                }

                if (flen > 0) {
                    for (String item : flts){
                        Double cur = Double.parseDouble(item);
                        if (max < cur) max = cur;
                        if (min > cur) min = cur;
                        sum += cur; 
                    }
                }
                avg = sum / (ilen + flen);

                out.print("numerics: min = " + min + ", max = " + max);
                out.println(", sum = " + sum + ", avg = " + avg);
            }

            if (slen > 0) {
                int max = strs[0].length(); 
                int min = max;

                for (String item : strs){
                    int cur = item.length();
                    if (max < cur) max = cur;
                    if (min > cur) min = cur;
                }

                out.print("strings: min length = " + min + ", max length = " + max);
            }
        }
    }   
}

