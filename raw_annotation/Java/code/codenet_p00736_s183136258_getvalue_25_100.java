import java.util.Scanner;
public class Main 
{
	static Scanner scan = new Scanner(System.in);
	static int getsimplecon(String minicon)
	{ 
		boolean not = false;
		while(minicon.charAt(0) == '-')
		{
			not = !not;
			minicon = minicon.substring(1);
		}
		int ans;
		if(not)
		{
			ans = 2-(Integer.parseInt(minicon));
			return ans;
		}
		else
		{
			ans = Integer.parseInt(minicon);
			return ans;
		}
	}
	static int getvalue(String content, int p, int q, int r, boolean replace)
	{
		int curdepth = 0;
		int startbracket = -1;
		if(replace)
		{
			content = content.replaceAll("P", Integer.toString(p));
			content = content.replaceAll("Q", Integer.toString(q));
			content = content.replaceAll("R", Integer.toString(r));
		}
		for(int i = 0; i < content.length(); i++)
		{
			char cur = content.charAt(i);
			if(cur == '(')
			{
				if(curdepth == 0)
				{
					startbracket = i;
				}
				curdepth += 1;
			}
			if(cur == ')')
			{
				curdepth -= 1;
				if(curdepth == 0)
				{
					String subcontent = content.substring(startbracket+1, i);
					String left = content.substring(0, startbracket);
					String right = content.substring(i+1);
					int subvalue = getvalue(subcontent, p, q, r, false);
					content = left + subvalue + right;
					i = startbracket;
				}
			}
		}
		for(int i = 0; i < content.length(); i++)
		{
			char cur = content.charAt(i);
			if(cur == '*' || cur == '+')
			{
				String leftcon = content.substring(0, i);
				String rightcon = "";
				int endofrightcon = -1; 
				for(int j = i+1; j < content.length(); j++)
				{
					char curj = content.charAt(j);
					if(curj == '*' || curj == '+')
					{
						rightcon = content.substring(i+1, j);
						endofrightcon = j-1;
						break;
					}
					else if(j == content.length()-1)
					{
						rightcon = content.substring(i+1);
						endofrightcon = j;
						break;
					}
				}
				int leftv = getsimplecon(leftcon);
				int rightv = getsimplecon(rightcon);
				int minires = -1;
				if(cur == '*')
				{
					minires = Math.min(leftv, rightv);
				}
				else if(cur == '+')
				{
					minires = Math.max(leftv, rightv);
				}
				content = minires + content.substring(endofrightcon+1);
				i = 0;
			}
		}
		return getsimplecon(content);
	}
	public static void main(String[] args) 
	{
		String s;
		while(true)
		{
			s = scan.next();
			int count = 0;
			if(s.equals("."))break;
			for(int p = 0; p <= 2; p++)
			{
				for(int q = 0; q <= 2; q++)
				{
					for(int r = 0; r <= 2; r++)
					{
						if(getvalue(s,p,q,r, true) == 2)
						{
							count++;
						}
					}
				}
			}
			System.out.println(count);
		}
	}
}