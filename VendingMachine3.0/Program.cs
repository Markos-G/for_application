using Newtonsoft.Json;

namespace VendingMachine
{
    abstract class CoinDispenser
    {
        protected CoinDispenser nextDispenser;

        public void SetNext(CoinDispenser nextDispenser)
        {
            this.nextDispenser = nextDispenser;
        }

        public abstract List<double> Dispence(double difference, Dictionary<double, int> pool);
        
    }

    internal class TwoPoundDispencer : CoinDispenser
    {
        public override List<double> Dispence(double difference, Dictionary<double , int> pool)
        {
            double denomination = 2;
            List<double> number = new List<double>();
            while (difference >= denomination && pool[denomination] > 0 )
            {
                pool[denomination]--;
                difference = Math.Round(difference - denomination,4);
                number.Add(denomination);
            }

            if (difference > 0 && nextDispenser != null)
            {
                number.AddRange(nextDispenser.Dispence(difference, pool));
            }
            else if (difference > 0)
            {
                throw new Exception("not enough change");
            }
            return number;
        }
    }

    internal class OnePoundDispencer : CoinDispenser
    {
        public override List<double> Dispence(double difference, Dictionary<double, int> pool)
        {
            double denomination = 1;
            List<double> number = new List<double>();
            while (difference >= denomination && pool[denomination] > 0)
            {
                pool[denomination]--;
                difference = Math.Round(difference - denomination, 4);
                number.Add(denomination);
            }

            if (difference > 0 && nextDispenser != null)
            {
                number.AddRange(nextDispenser.Dispence(difference, pool));
            }
            else if (difference > 0)
            {
                throw new Exception("not enough change");
            }
            return number;
        }
    }

    internal class FiftyPenceDispencer : CoinDispenser
    {
        public override List<double> Dispence(double difference, Dictionary<double, int> pool)
        {
            double denomination = 0.5;
            List<double> number= new List<double>();
            while (difference >= denomination && pool[denomination] > 0)
            {
                pool[denomination]--;
                difference = Math.Round(difference - denomination, 4);
                number.Add(denomination);
            }

            if (difference > 0 && nextDispenser != null)
            {
                number.AddRange(nextDispenser.Dispence(difference, pool));
            }
            else if (difference > 0)
            {
                throw new Exception("not enough change");
            }
            return number;
        }
    }

    internal class TwentyPenceDispencer : CoinDispenser
    {
        public override List<double> Dispence(double difference, Dictionary<double, int> pool)
        {
            double denomination = 0.2;
            List<double> number = new List<double>();
            while (difference >= denomination && pool[denomination] > 0)
            {
                pool[denomination]--;
                difference = Math.Round(difference - denomination, 4);
                number.Add(denomination);
            }

            if (difference > 0 && nextDispenser != null)
            {
                number.AddRange(nextDispenser.Dispence(difference, pool));
            }
            else if (difference > 0)
            {
                throw new Exception("not enough change");
            }
            return number;
        }
    }

    internal class TenPenceDispencer : CoinDispenser
    {
        public override List<double> Dispence(double difference, Dictionary<double, int> pool)
        {
            double denomination = 0.1;
            List<double> number = new List<double>();
            while (difference >= denomination && pool[denomination] > 0)
            {
                pool[denomination]--;
                difference = Math.Round(difference - denomination, 4);
                number.Add(denomination);
            }

            if (difference > 0 && nextDispenser != null)
            {
                number.AddRange(nextDispenser.Dispence(difference, pool));
            }
            else if (difference > 0)
            {
                throw new Exception("not enough change");
            }
            return number;
        }
    }

    internal class FivePenceDispencer : CoinDispenser
    {
        public override List<double> Dispence(double difference, Dictionary<double, int> pool)
        {
            double denomination = 0.05;
            List<double> number = new List<double>();
            while (difference >= denomination && pool[denomination] > 0)
            {
                pool[denomination]--;
                difference = Math.Round(difference - denomination, 4);
                number.Add(denomination);
            }

            if (difference > 0 && nextDispenser != null)
            {
                number.AddRange(nextDispenser.Dispence(difference, pool));
            }
            else if (difference > 0)
            {
                throw new Exception("not enough change");
            }
            return number;
        }
    }



    internal class VendingMachine: IVendingMachine
    {

        static void Main(string[] args)
        {
            VendingMachine machine = new VendingMachine();
            List<Snack> snacks = new List<Snack>
            {
                new Snack("Cola", 10, 1.5),
                new Snack("Choc Bar", 10, 1.25),
                new Snack("Skittles", 8, 1.7),
                new Snack("Bikkies", 10, 1.25),
                new Snack("Gala", 4, 1.25)
            };

            Dictionary<double, int> changePool = new Dictionary<double, int> {{ 2, 2 },
                                                                              { 1, 3 },
                                                                              { 0.5, 4 },
                                                                              { 0.2, 5},
                                                                              { 0.1, 10 },
                                                                              { 0.05, 20}
                                                                                        };

            string dbFileSnacks = "snacks.json";
            string dbFileCoins = "coins.json";
            
            // if file exists then read from file -> simulating database
            if (File.Exists(dbFileSnacks))
            {
                string jsonSnacks = File.ReadAllText(dbFileSnacks);
                snacks = JsonConvert.DeserializeObject<List<Snack>>(jsonSnacks);
            }
            if (File.Exists(dbFileCoins))
            {
                string jsonCoins = File.ReadAllText(dbFileCoins);
                changePool = JsonConvert.DeserializeObject<Dictionary<double, int>>(jsonCoins);
            }

            User user = User.customer;
            do
            {
                if (user == User.customer)
                {
                    machine.Header(snacks);
                    string option = Console.ReadLine();
                    int optionToInt = 0;
                    try
                    { 
                        optionToInt = Convert.ToInt32(option); 
                    }
                    catch
                    { 
                    }

                    if (optionToInt >= 1 && optionToInt <= 5)
                    {
                        // if there is not enough snacks to give
                        if (snacks[optionToInt - 1].quantity == 0)
                        {
                            Console.WriteLine("out of stock");
                        }
                        // else if there are enought snacks
                        else
                        {
                            Console.WriteLine("Enter change in £2s, £1s, £0.50s, £0.20s, £0.10 or £0.05");
                            double sum = 0;
                            int[] cashInserted = new int[6];
                            int i = 0;
                            foreach (double typeOfCoin in changePool.Keys)
                            {
                                Console.WriteLine("how many £" + typeOfCoin + "s: ");
                                // coins from the user
                                cashInserted[i] = Convert.ToInt32(Console.ReadLine());
                                sum += cashInserted[i] * typeOfCoin;
                                i++;
                            }
                            // if cash inserted are enough to buy it
                            if (sum >= snacks[optionToInt - 1].price)
                            {
                                double difference = sum - snacks[optionToInt - 1].price;
                                if (machine.GiveChange(difference, changePool, cashInserted))
                                {
                                    // then and only then reduce quantity
                                    snacks[optionToInt - 1].quantity -= 1;
                                }
                                else
                                {
                                    Console.WriteLine("Not enough change to give back");
                                }
                            }
                            else
                            {
                                Console.WriteLine("Not enough money to purchace.");

                            }
                        }
                    }
                    if (option == "q")
                    {
                        machine.Quit(snacks, changePool, dbFileSnacks, dbFileCoins);
                        break;
                    }
                    if (option == "1011")
                    {
                        Console.WriteLine("Enter password: ");
                        string password = Console.ReadLine();
                        if (password == "A5144I")
                        {
                            user = User.admin;
                        }
                        else
                        {
                            Console.WriteLine("Going back to menu");
                            continue;
                        }
                    }
                }
                if (user == User.admin)
                {
                    machine.Header();
                    string option = Console.ReadLine();
                    if (option == "1")
                    {
                        machine.ChangePrices(snacks);
                    }
                    else if(option == "2")
                    {
                        machine.AddChange(changePool);
                    }
                    else if (option == "3")
                    {
                        machine.GenerateReport(changePool);
                    }
                    else if (option == "0")
                    {
                        user = User.customer;
                    }
                    else if (option == "q")
                    {
                        machine.Quit(snacks, changePool, dbFileSnacks, dbFileCoins);
                        break;
                    }
                    
                }
            }
            while (true);
        }
        public void Header(List<Snack> snacks)
        {
            Console.WriteLine("#################################");
            Console.WriteLine("#  Mecachrome Vending Merchant  #");
            Console.WriteLine(" #    Hawking Edible Wares     #");
            Console.WriteLine("  #############################");
            Console.WriteLine("   Snack    -- Price  -- QTY");
            string[] customPadding = { "     ", " ", " ", "  ", "     " };
            for (int i = 0; i < snacks.Count(); i++)
            {
                if (snacks[i].quantity > 0)
                {
                    Console.WriteLine((i + 1) + ". " + snacks[i].label + customPadding[i] + "-- " + "£" + snacks[i].price.ToString("0.00") + "  --  " + snacks[i].quantity.ToString("D2"));
                }
                else
                {
                    Console.WriteLine((i + 1) + ". " + snacks[i].label + customPadding[i] + "-- " + "£" + snacks[i].price.ToString("0.00") + "  --  " + "outOfStock");
                }
            }
            Console.WriteLine("    Please enter choice: ");
            Console.WriteLine("     press 'q' to quit");
        }

        public void Header()
        {
            Console.WriteLine("#########################");
            Console.WriteLine(" 1. change snack prices");
            Console.WriteLine(" 2. increase change pool");
            Console.WriteLine(" 3. report amount");
            Console.WriteLine(" press 0 to go back ");
            Console.WriteLine(" press 'q' to quit ");
        }

        public bool GiveChange(double difference, Dictionary<double, int> pool, int[] cashInserted)
        {
            // keep a copy to revert changes
            Dictionary<double, int> copycoins = new Dictionary<double, int>(pool);
            // add also the inserted coins to the same type pool of coins in the machine
            int i = 0;
            foreach (double typeOfCoin in pool.Keys)
            {
                pool[typeOfCoin] += cashInserted[i];
                i++;
            }

            TwoPoundDispencer twoPoundDispencer = new TwoPoundDispencer();
            OnePoundDispencer onePoundDispencer = new OnePoundDispencer();
            FiftyPenceDispencer fiftyPenceDispencer = new FiftyPenceDispencer();
            TwentyPenceDispencer twentyPenceDispencer = new TwentyPenceDispencer();
            TenPenceDispencer tenPenceDispencer = new TenPenceDispencer();
            FivePenceDispencer fivePenceDispencer = new FivePenceDispencer();

            twoPoundDispencer.SetNext(onePoundDispencer);
            onePoundDispencer.SetNext(fiftyPenceDispencer);
            fiftyPenceDispencer.SetNext(twentyPenceDispencer);
            twentyPenceDispencer.SetNext(tenPenceDispencer);
            tenPenceDispencer.SetNext(fivePenceDispencer);
            //fivePenceDispencer.SetNext(null);
            bool enoughchange = true;
            try
            {
                List<double> numbers = twoPoundDispencer.Dispence(difference, pool);
                var g = numbers.GroupBy(i => i);

                foreach (var grp in g)
                {
                    Console.WriteLine("{0}'s given back: {1}", grp.Key, grp.Count());
                }
            }
            catch
            {
                enoughchange = false;
            }

            // revert changes here --/-- 'pool = copycoins' doesnt work for some reason
            // have to do it explicitly
            if (!enoughchange)
            {
                foreach (KeyValuePair<double, int> type in copycoins)
                {
                    pool[type.Key] = copycoins[type.Key];
                }
            }
            return enoughchange;
        }

        public void ChangePrices(List<Snack> snacks)
        {
            Console.WriteLine("Enter id number of product to change its price");
            int id = Convert.ToInt32(Console.ReadLine());
            double newprice = 0;
            while (newprice <= 0)
            {
                Console.WriteLine("change price for: " + snacks[id - 1].label);
                newprice = Convert.ToDouble(Console.ReadLine());
            }
            snacks[id - 1].price = newprice;
        }

        public void AddChange(Dictionary<double, int> pool)
        {
            foreach (double typeOfCoin in pool.Keys)
            {
                int add = -1;
                while (add < 0)
                {
                    Console.WriteLine("number of " + typeOfCoin + "s to add: ");
                    add = Convert.ToInt32(Console.ReadLine());
                }
                pool[typeOfCoin] += add; 
            }
        }

        public void GenerateReport(Dictionary<double, int> pool)
        {
            foreach (KeyValuePair<double, int> type in pool)
            {
                Console.WriteLine("number of " + type.Key + "s: " + type.Value);
            }
        }

        public void Quit(List<Snack> snacks, Dictionary<double, int> coins, string dbfile, string dbfile2)
        {
            string jsonString = JsonConvert.SerializeObject(snacks, Formatting.Indented);
            string jsonString2 = JsonConvert.SerializeObject(coins, Formatting.Indented);
            File.WriteAllText(dbfile, jsonString);
            File.WriteAllText(dbfile2, jsonString2);
        }

    }
}