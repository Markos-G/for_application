//using System.Text.Json;
using Newtonsoft.Json;

namespace ConsoleApp2 
{
    internal class WestminsterHotel : IHotelManager, IHotelCustomer
    {

        private Dictionary<int, Room> rooms = new Dictionary<int, Room>();
        
            
        static void Main(string[] args)
        {

            WestminsterHotel hotel = new WestminsterHotel();
            string dbfile = "db.json";
            JsonSerializerSettings settings = new JsonSerializerSettings { TypeNameHandling = TypeNameHandling.All };
            if (File.Exists(dbfile))
            {
                string json = File.ReadAllText(dbfile);
                hotel.rooms = JsonConvert.DeserializeObject<Dictionary<int, Room>>(json, settings);
            }


            User user = User.customer;
            do
            {
                if (user == User.customer)
                {
                    Console.WriteLine("press 1 for listAvailableRooms");
                    Console.WriteLine("press 2 for listAvailableRooms based on maxPrice");
                    Console.WriteLine("press 3 for bookRoom");
                    Console.WriteLine("press 4 for admin privileges");
                    Console.WriteLine("press 'q' to quit");
                    string option = Console.ReadLine();
                    if (option == "1")
                    {
                        Console.WriteLine("enter check-in date DD/MM/YYYY");
                        DateTime check_in = DateTime.Parse(Console.ReadLine());
                        Console.WriteLine("enter check-out date DD/MM/YYYY");
                        DateTime check_out = DateTime.Parse(Console.ReadLine());
                        int compare = DateTime.Compare(check_in, check_out);
                        if (compare < 0)
                        {
                            Booking dates = new Booking(check_in, check_out);
                            Console.WriteLine("enter 1 for signle, 2 for double, 3 for triple size room");
                            Size size = (Size)Enum.Parse(typeof(Size), Console.ReadLine(), true);
                            hotel.ListAvailableRooms(dates, size);
                        }
                        else if (compare >= 0)
                        {
                            Console.WriteLine("wrong dates");
                        }
                    }
                    else if (option == "2")
                    {
                        Console.WriteLine("enter check-in date DD/MM/YYYY");
                        DateTime check_in = DateTime.Parse(Console.ReadLine());
                        Console.WriteLine("enter check-out date DD/MM/YYYY");
                        DateTime check_out = DateTime.Parse(Console.ReadLine());
                        int compare = DateTime.Compare(check_in, check_out);
                        if (compare < 0)
                        {
                            Booking dates = new Booking(check_in, check_out);
                            Console.WriteLine("enter 1 for signle, 2 for double, 3 for triple size room");
                            Size size = (Size)Enum.Parse(typeof(Size), Console.ReadLine(), true);
                            Console.WriteLine("enter max price");
                            int maxPrice = Convert.ToInt32(Console.ReadLine());
                            hotel.ListAvailableRooms(dates, size, maxPrice);
                        }
                        else if (compare >= 0)
                        {
                            Console.WriteLine("wrong dates");
                        }
                    }
                    else if (option == "3")
                    {
                        Console.WriteLine("enter check-in date DD/MM/YYYY");
                        DateTime check_in = DateTime.Parse(Console.ReadLine());
                        Console.WriteLine("enter check-out date DD/MM/YYYY");
                        DateTime check_out = DateTime.Parse(Console.ReadLine());
                        int compare = DateTime.Compare(check_in, check_out);
                        if (compare < 0)
                        {
                            Booking dates = new Booking(check_in, check_out);
                            Console.WriteLine("enter room number to book");
                            int roomNumber = Convert.ToInt32(Console.ReadLine());
                            hotel.BookRoom(roomNumber, dates);
                        } 
                        else if (compare >= 0)
                        {
                            Console.WriteLine("wrong dates");
                        }                              
                    }
                    else if (option == "4")
                    {
                        user = User.admin;
                    }
                    else if (option == "q")
                    {
                        hotel.Quit(hotel.rooms, dbfile, settings);
                        break;
                    }
                    else
                    {
                        Console.WriteLine("wrong input: going back to menu");
                        continue;
                    }
                }
                if (user == User.admin)
                {
                    Console.WriteLine("press 1 for AddRoom");
                    Console.WriteLine("press 2 for DeleteRoom");
                    Console.WriteLine("press 3 for ListRooms");
                    Console.WriteLine("press 4 for ListRoomsOrderedByPrice");
                    Console.WriteLine("press 5 to GenerateReport");
                    Console.WriteLine("press 0 to go back");
                    Console.WriteLine("press 'q' to quit");
                    string option = Console.ReadLine();
                    if (option == "1")
                    {
                        hotel.CreateRoomWorkflow();
                    }
                    else if (option == "2")
                    {
                        Console.WriteLine("enter room number to delete it");
                        hotel.DeleteRoom(Convert.ToInt32(Console.ReadLine()));
                    }
                    else if (option == "3")
                    {
                        hotel.ListRooms();
                    }
                    else if (option == "4")
                    {
                        hotel.ListRoomsOrderedByPrice();
                    }
                    else if (option == "5")
                    {
                        string fileName = "ROOMS.json";
                        hotel.GenerateReport(fileName);
                    }
                    else if (option == "0")
                    {
                        user = User.customer;
                    }
                    else if (option == "q")
                    {
                        hotel.Quit(hotel.rooms, dbfile, settings);
                        break;
                    }
                    else
                    {
                        Console.WriteLine("wrong input: going back to menu");
                        continue;
                    }
                }
            }
            while (true);
        }

        public void Quit(Dictionary<int, Room> dict, string dbfile, JsonSerializerSettings settings)
        {
            string jsonString = JsonConvert.SerializeObject(dict, settings);
            File.WriteAllText(dbfile, jsonString);
        }
        public void CreateRoomWorkflow()
        {
            Console.WriteLine("enter room number");
            int number = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("enter floor number");
            int floor = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("enter 1 for single, 2 for double,3 for triple size room");
            Size size = (Size)Enum.Parse(typeof(Size), Console.ReadLine(), true);
            Console.WriteLine("enter price");
            double price = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("press 1 for standard or 2 for deluxe");
            string type = Console.ReadLine();
            Room room;
            if (type == "1")
            {
                Console.WriteLine("enter number of windows");
                int windows = Convert.ToInt32(Console.ReadLine());
                room = new StandardRoom(number, floor, size, price, windows);
                AddRoom(room);
            }
            else if (type == "2")
            {
                Console.WriteLine("enter 1 for sea view, 2 for mountain view, 3 for landmark view");
                View view = (View)Enum.Parse(typeof(View), Console.ReadLine(), true);
                Console.WriteLine("enter m2 for balcony size");
                double balcony = Convert.ToDouble(Console.ReadLine());
                room = new DeluxeRoom(number, floor, size, price, view, balcony);
                AddRoom(room);
            }
        }
        public bool AddRoom(Room room)
        {
            try
            {
                rooms.Add(room.number, room);
                return true;
            }
            catch
            {
                Console.WriteLine("room exists");
                return false;
            }
        }
        public bool DeleteRoom(int roomNumber)
        {
            try
            {
                Console.WriteLine(rooms[roomNumber]);
                Console.WriteLine("room with above info deleted");
                return rooms.Remove(roomNumber);
            }
            catch
            {
                Console.WriteLine("room doesn't exist");
                return false;
            }
        }
        public void ListRooms()
        {
            foreach (Room r in rooms.Values)
            {
                Console.WriteLine(r);
            }
        }
        public void ListRoomsOrderedByPrice()
        {
            List<Room> descending = new List<Room>();
            foreach (KeyValuePair<int, Room> room in rooms.OrderBy(key => key.Value.price))
            {
                descending.Add(room.Value);
            }
            for (int i = descending.Count(); i > 0; i--)
            {
                Console.WriteLine(descending[i - 1]);
            }
        }
        public void GenerateReport(string fileName)
        {
            string jsonString = JsonConvert.SerializeObject(rooms, Formatting.Indented);
            File.WriteAllText(fileName, jsonString);
        }
        public void ListAvailableRooms(Booking wantedBooking, Size roomSize)
        {
            foreach (Room room in rooms.Values)
            {
                if (room.size == roomSize)
                {
                    
                    if (room.bookings.Count() == 0)
                    {
                        Console.WriteLine(room);
                    }
                    else
                    {
                        bool flag = false;
                        foreach (Booking booking in room.bookings)
                        {
                            if (!booking.Overlaps(wantedBooking))
                            {
                                flag = true;
                                break;
                            }
                        }
                        if (flag)
                        {
                            Console.WriteLine(room);
                        }
                    }
                }
            }
        }
        public void ListAvailableRooms(Booking wantedBooking, Size roomSize, int maxPrice)
        {
            List<Room> forSorting = new List<Room>();
            foreach (Room room in rooms.Values)
            {
                if (room.size == roomSize && room.price < maxPrice)
                {
                    if (room.bookings.Count() == 0)
                    {
                        forSorting.Add(room);
                    }
                    else
                    {
                        bool flag = false;
                        foreach (Booking booking in room.bookings)
                        {
                            if (!booking.Overlaps(wantedBooking))
                            {
                                flag = true;
                                break;
                            }
                        }
                        if (flag)
                        {
                            forSorting.Add(room);
                        }
                    }
                }
            }
            forSorting.Sort();
            foreach (Room room in forSorting)
            {
                Console.WriteLine(room);
            }
        }
        public bool BookRoom(int roomNumber, Booking wantedBooking)
        {
            try
            {
                bool flag = true;
                foreach (Booking booking in rooms[roomNumber].bookings)
                {
                    if (wantedBooking.Overlaps(booking))
                    {
                        Console.WriteLine("dates overlap, can't book");
                        flag = false;
                        break;
                    }
                }
                if (flag)
                {
                    Console.WriteLine("room booked");
                    rooms[roomNumber].AddBooking(wantedBooking);
                }
                return flag;
            }
            catch
            {
                Console.WriteLine("no such room exists");
                return false;
            }
        }
    }
}


