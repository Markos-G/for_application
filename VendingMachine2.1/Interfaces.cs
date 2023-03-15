namespace VendingMachine;

interface IVendingMachine
{
    bool GiveChange(double difference, Dictionary<double, int> pool, int[] cashInserted);
    void ChangePrices(Snack snacks);
    void AddChange(Dictionary<double, int> pool);
    void GenerateReport(Dictionary<double, int> pool);

}

//interface ICoinDispenser
//{
//    void SetNext(ICoinDispenser nextCoinDispenser);
//    void Dispence(double amount, Dictionary<double, int> changePool);
//}

