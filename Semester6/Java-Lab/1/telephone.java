import java.util.*;
import java.io.*;

class MissedCall 
{
	String name, phoneNo, time;
	MissedCall(String n, String p, String t)
	{
		name = n;
		phoneNo = p;
		time = t;
	}

	public String toString() // To convert object in string if not used then print command will print garbage values
	{
		return "\nName: " + name + "\nPhone No: " + phoneNo + "\nTime: " + time;
	}
}
class Caller
{
	int id;
	String name_a, phoneNo_a;

	Caller(int k, String n, String p)
	{
		id = k;
		name_a = n;
		phoneNo_a = p;
	}
}

public class telephone
{
	public static void main(String[] args)
	{
		int count = 0;
		Scanner sc = new Scanner(System.in);
		Calendar c = Calendar.getInstance();
		ArrayList<Caller> alist = new ArrayList<Caller>(); // Array List that contains dummy data
		ArrayList<MissedCall> mlist = new ArrayList<MissedCall>(); // Missed Call List that randomly fetches values from alist
		alist.add(new Caller(1, "Ishank 1", "1234"));
		alist.add(new Caller(2, "Ishank 2", "5678"));
		alist.add(new Caller(3, "Ishank 3", "9012"));
		alist.add(new Caller(4, "Ishank 4", "3456"));
		alist.add(new Caller(5, "Private", "Not available"));
		alist.add(new Caller(6, "Private", "Not available"));
		alist.add(new Caller(7, "Private", "Not available"));

		while(true)
		{
			System.out.println("\n1) Add\n2) Call History\n3) Delete\n4) Exit: ");
			int ch = sc.nextInt();
			switch(ch)
			{
				case 1:
				if(count > 10)
				{
					mlist.remove(0); // Remove first element as soon as count of missed calls reaches > 10
					count--;
				}
				Random rand = new Random();
				int randomNumber = rand.nextInt(7);
				Caller caller = alist.get(randomNumber); // Random caller object generated
				int H = c.get(Calendar.HOUR);
				int M = c.get(Calendar.MINUTE);
				int S = c.get(Calendar.SECOND);
				String time1 = H + ":" + M + ":" + S;
				mlist.add(new MissedCall(caller.name_a, caller.phoneNo_a, time1)); // adding the random caller to mlist
				count++;
				System.out.println("Name - "+caller.name_a + "\nPhone " +caller.phoneNo_a +" \nAdded successfully" );
				break;

				case 2:
				for(int i = 0; i < mlist.size(); i++)
				{	
					System.out.println("***Call Logs***");
					MissedCall missedCaller = mlist.get(i);
					System.out.println("\nName: " + missedCaller.name + "\nPhone No: " + missedCaller.phoneNo + "\nTime: " + missedCaller.time);
					if(i == mlist.size() -1 ){
					System.out.println("***Last record reached next record not available!***");
				}
					System.out.println("\n1) Display next\n2) Display next and delete current: ");
					int ch1 = sc.nextInt();
					switch(ch1)
					{
						case 1:
						continue;

						case 2:
						System.out.println(mlist.get(i) + " -- deleted successfully\n");
						mlist.remove(i);
						i--;
						count--;
						continue;
					}
				}
				break;

				case 3:
				System.out.println("\nEnter number to delete: ");
				Scanner sc1 = new Scanner(System.in); // created another scanner object again as it was not taking the previous scanner object (idk why)
				String delNum = sc1.nextLine();
				for(int i = 0; i < mlist.size(); i++)
				{
					MissedCall missedCaller = mlist.get(i);
					if(missedCaller.phoneNo.equals(delNum))
					{
						mlist.remove(i);
						count--;
						System.out.println("Deleted! (" + delNum + ")");
					}
				}
				break;

				case 4:
				System.exit(0);
			}
		}
	}
}