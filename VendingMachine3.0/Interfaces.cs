namespace VendingMachine;

interface IVendingMachine
{
    bool GiveChange(double difference, Dictionary<double, int> pool, int[] cashInserted);
    void ChangePrices(List<Snack> snacks);
    void AddChange(Dictionary<double, int> pool);
    void GenerateReport(Dictionary<double, int> pool);

}


