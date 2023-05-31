A Hotel needs a software system to operate their business moreefficiently and automate the booking process of the rooms of their Hotel.
Users: The system is expected to work with two types of users:• a customer can use it to check the list of rooms that are available onspecific dates and to make bookings accordingly.
       An admin can add and delete rooms, print rooms information, etc.
Types of Rooms: The hotel has two types of Room: StandardRoom, and DeluxeRoom. All theRooms have a unique room Number, Floor, Size (either single, double or triple) and Price (per night). 
                Moreover, a StandardRoom has a given numberof Windows (at least 1); a DeluxeRoom room has a Balcony (of a given size inm2) and a View (either seaview, landmark view, or mountain view).
Booking a Room: The system should keep track of the dates when each Room has been booked. We assume that a Booking consists of a check-in and check-out date. 
                For simplicity only consider the date as a combination of day, monthand year (do not include the time) and make sure that the check-in date isalways before a check-out date.
                A Room can have multiple Bookings, if they do not overlap.For instance, Room1 can have 2 bookings: booking1 with check-in on10/11/2022, check-out on 15/11/2022 and booking2 with check-in on15/11/2022, check-out on 18/11/2021.
                Two Booking objects  may not overlap
