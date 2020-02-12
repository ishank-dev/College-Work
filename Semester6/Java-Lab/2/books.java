import java.util.*;
import java.io.*;

class bookList
{	String title,author,publisher,price;
	bookList(String t,String a,String p,String pr ){
		title = t;
		author = a;
		publisher = p;
		price = pr;
	}
	public String toString() 
	{
		return "\nTitle: " + title + "\nAuthor " + author + "\nPublisher" + publisher + "\nPrice" + price;
	}		
}

public class books
{
	public static void main(String[] args)
	{	
		int count = 0;
		Scanner sc = new Scanner(System.in);
		ArrayList<bookList> alist = new ArrayList<bookList>();
		ArrayList<bookList> blist = new ArrayList<bookList>();
		alist.add(new bookList("Title 1", "Author 1", "Publisher 1", "Price 1"));
		alist.add(new bookList("Title 2", "Author 2", "Publisher 2", "Price 2"));
		alist.add(new bookList("Title 3", "Author 3", "Publisher 3", "Price 3"));
		alist.add(new bookList("Title 4", "Author 4", "Publisher 4", "Price 4"));
	
		while(true){
			System.out.println("\n1)Add Books\n2)Display Books in normal order\n3)Display Books in sorted order ");
			int ch = sc.nextInt();
			switch(ch)
			{
				case 1:
				
				Random rand = new Random();
				int randomNumber = rand.nextInt(4);
				bookList book1 = alist.get(randomNumber);
				blist.add(new bookList(book1.title,book1.author,book1.publisher,book1.price)); 
				count++;
				System.out.println("\nTitle: " + book1.title + "\nAuthor " + book1.author + "\nPublisher" + book1.publisher+"\nPrice" + book1.price + "\nAdded successfully");
				break;

				case 2:
				System.out.println("***Book Details***");
				for(int i = 0; i < blist.size(); i++)
				{
					System.out.println(blist.get(i));
				}
				break;
			
				// case 3:
				// ArrayList<bookList> blist1 = new ArrayList<bookList>(blist);
				// Collections.sort(blist);
				// for(int i = 0; i < blist.size(); i++)
				// {	
				// 	System.out.println(blist.get(i));
				// }

			}
		}
	}
}

