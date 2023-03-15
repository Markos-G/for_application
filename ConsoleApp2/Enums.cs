using Newtonsoft.Json.Converters;

[Newtonsoft.Json.JsonConverter(typeof(StringEnumConverter))]
public enum User 
{
    customer = 0,
    admin = 1
}
[Newtonsoft.Json.JsonConverter(typeof(StringEnumConverter))]
public enum Size
{
    singleroom = 1,
    doubleroom = 2,
    tripleroom = 3
}
[Newtonsoft.Json.JsonConverter(typeof(StringEnumConverter))]
public enum View
{
    seaview = 0,
    mountainview = 1,
    landmarkview  = 2
}