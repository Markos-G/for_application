namespace VendingMachine
{
    internal class Snack
    {

        private string _label;
        public string label { get { return _label; } set { _label = value; } }

        private int _quantity;
        public int quantity { get { return _quantity; } set { _quantity = value; } }
        private double _price;
        public double price { get { return _price; } set { _price = value; } }




        public Snack(string label, int quantity, double price)
        {
            this.label = label;
            this.quantity = quantity;
            this.price = price;

        }

    }
} 
     