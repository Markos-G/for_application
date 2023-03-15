namespace ConsoleApp2
{
    internal class Booking : IOverlappable
    {
        private DateTime _check_in = new DateTime();
        private DateTime _check_out = new DateTime();

        public DateTime check_in { get { return _check_in; } set { _check_in = value; } }
        public DateTime check_out { get { return _check_out; } set { _check_out = value; } }

        public Booking(DateTime d1, DateTime d2)
        {
            check_in = d1;
            check_out = d2;
        }
        public bool Overlaps(Booking other)
        {
            if (this.check_in < other.check_out && this.check_out > other.check_in)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        public override string ToString()
        {
            return $"check-in {check_in.ToShortDateString()} " +
                   $"check-out {check_out.ToShortDateString()}";
        }
    }
}
