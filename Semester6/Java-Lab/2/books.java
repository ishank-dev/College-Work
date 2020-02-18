//Work in progress
import java.util.*;


class Book implements Comparable<Book> {

    String title, author, publisher;
    Double price;
    Book(String t, String aut, String pub, Double pr) {
        title = t;
        author = aut;
        publisher = pub;
        price = pr;
    }
    
    Double getPrice() {
        return price;
    }
    
    public String toString() {
        return "\nTitle: " + title + "\nAuthor: " + author + "\nPublisher:" + publisher + "\nPrice:" + price;
    }
    
    public int compareTo(Book b) {
        return getPrice().compareTo(b.getPrice());
    }
}
public class books
{
	public static void main(String[] args)
	{	
		Scanner sc = new Scanner(System.in);
		ArrayList<Book> alist = new ArrayList<Book>();
		ArrayList<Book> blist = new ArrayList<Book>();
		alist.add(new Book("Three man in a boat", "Jerome K. Jerome", "J. W. Arrowsmith", 123.12));
		alist.add(new Book("The Diary of a young girl", "Anne Frank", "Contact Publishing", 12346.23));
		alist.add(new Book("50 Shades of Grey", "E. L. James", "Vintage Books", 12345.14));
		while(true){
			System.out.println("\n1)Add Books\n2)Display Books in normal order\n3)Sort books by price ");
			int ch = sc.nextInt();
			switch(ch)
			{
				case 1:
				Random rand = new Random();
				int randomNumber = rand.nextInt(3);
				Book bookObj = alist.get(randomNumber);
				blist.add(new Book(bookObj.title,bookObj.author,bookObj.publisher,bookObj.price)); 
				System.out.println("\nTitle: " + bookObj.title + "\nAuthor: " + bookObj.author + "\nPublisher: " + bookObj.publisher+"\nPrice: " + bookObj.price + "\n**Added successfully**");
				break;

				case 2:
				System.out.println("*****Book Details*****");
				for(int i = 0; i < blist.size(); i++)
				{
					System.out.println(blist.get(i));
				}
				break;
			
				case 3:
				ArrayList<Book> slist = new ArrayList<Book>(blist);
        		Collections.sort(slist);
				System.out.println("****Sorted List****");
				for(int i = 0; i < slist.size(); i++)
				{
					System.out.println(slist.get(i));
				}

			}
		}
	}
}

