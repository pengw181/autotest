import java.io.*;
 
public class readfilejd {
    public static void main(String[] args)  {
        try {
            InputStreamReader isr = new InputStreamReader(new FileInputStream("/mnt/shared/AiSee_FileNode/116-9312/440100_AiSeeCore/personal/pw自动化测试一级目录/request.txt"), "UTF-8");
	    BufferedReader in = new BufferedReader(isr);
            String str;
            while ((str = in.readLine()) != null) {
                System.out.println(str);
            }
            System.out.println(str);
        } catch (IOException e) {
        }
    }
}
























































































