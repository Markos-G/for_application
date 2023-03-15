namespace ConsoleApp2;
interface IHotelManager
{
    bool AddRoom(Room room);
    bool DeleteRoom(int roomNumber);
    void ListRooms();
    void ListRoomsOrderedByPrice();
    void GenerateReport(string fileName);
}

interface IHotelCustomer
{
    void ListAvailableRooms(Booking wantedBooking, Size roomSize);
    void ListAvailableRooms(Booking wantedBooking, Size roomSize, int maxPrice);
    bool BookRoom(int roomNumber, Booking wantedBooking);
}

interface IOverlappable
{
    bool Overlaps(Booking other);
}