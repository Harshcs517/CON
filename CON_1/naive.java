import java.util.*;

    class Distinct{
        public String word;
        public int numInbas;
        public int numInhoc;
    }
public class naive {

    public static void diff_words(LinkedList words,File fname)
    {
        BufferedReader reader = new BufferedReader(new FileReader(fname));
        String temp = reader.readLine();
        Distinct p = new Distinct();
        int j;
        while(temp != null)
        {       
            String[] split = temp.split(" ",0);
            for(int i=0;i<split.length;i++)
            {
                for(j=0;j<words.size();j++)
                {
                    if(words.get(j)==split[i])
                    {
                        break;
                    }
                }
                if(j==words.size())
                {
                    p.word = split[i];
                    words.add(p);
                }
            }
            temp = reader.readLine();
        }
    }
    public static void main(String[] args) {
        LinkedList<Distinct> words = new LinkedList<Distinct>();
        diff_words(words,"20ng-sports.txt");
        System.out.println(words.size());
    }
}