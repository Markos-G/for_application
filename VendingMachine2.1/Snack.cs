namespace VendingMachine
{
    internal class Snack
    {
        private string[] _label;
        public string[] label { get { return _label; } set { _label = value; } }
        private int[] _quantity;
        public int[] quantity { get { return _quantity; } set { _quantity = value; } }
        private double[] _price;
        public double[] price { get { return _price; } set { _price = value; } }


        public Snack()
        {
            label = new string[] { "Cola", "Choc Bar", "Skittles", "Bikkies", "Gala" };
            quantity = new int[] { 10, 10, 8, 10, 4 };
            price = new double[] { 1.50, 1.25, 1.70, 1.25, 1.25 };
        }


    }
} 
     