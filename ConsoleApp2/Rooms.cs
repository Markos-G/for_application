namespace ConsoleApp2
{
    internal class Room : IComparable<Room>
    {
        private int _number;
        public int number { get { return _number; } set { _number = value; } }
        private int _floor;
        public int floor { get { return _floor; } set { _floor = value; } }
        private Size _size;
        public Size size { get { return _size; } set { _size = value; } }
        private double _price;
        public double price { get { return _price; } set { _price = value; } }
        private List<Booking> _bookings;
        public List<Booking> bookings { get { return _bookings; } set { _bookings = value; } }
        public Room(int n, int f, Size s, double p)
        {
            number = n;
            floor = f;
            size = s;
            price = p;
            bookings = new List<Booking>();
        }
        public void AddBooking(Booking dates)
        {
            bookings.Add(dates);
        }

        public int CompareTo(Room other)
        {
            if (this.price < other.price)
            {
                return -1;
            }
            else if (this.price > other.price)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        public override string ToString()
        {
            string info = $"number: {number}" +
                $" floor: {floor}" +
                $" size: {size}" +
                $" price: {price}";
                foreach(Booking booking in bookings)
                {
                    info += $" booking: {booking} ";
                }
            return info;
                
        }
    }

    internal class StandardRoom : Room
    {
        private int _windows;
        public int windows { get { return _windows; } set { _windows = value; } }

        public StandardRoom(int n, int f, Size s, double p, int w) 
            :base(n, f, s, p)
        {
            if (w > 1)
            {
                windows = w;
            }
            else
            {
                windows = 1; 
            }
        }
        public override string ToString()
        {
            return base.ToString()+
                $" number of windows: {windows}";

        }

    }

    internal class DeluxeRoom : Room
    {
        private double _balcony;
        public double balcony { get { return _balcony; } set { _balcony = value; } }
        private View _view;
        public View view { get { return _view; } set { _view = value; } }
        public DeluxeRoom(int n, int f, Size s, double p, View v, double b)
            : base(n, f, s, p)
        {
            view = v;
            balcony = b;
        }
        public override string ToString()
        {
            return base.ToString() +
                $" view: {view}" +
                $" balcony: {balcony}";

        }

    }

}