dateElement = document.querySelector("#birthdate");
dateElement.addEventListener('input',function(){
    var dateValue = dateElement.value;
    var pattern = /^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])$/;
    if (pattern.test(dateValue))
    {
        var color = "#00ff00";
        dateElement.style.borderColor = color;
    };
    if (dateValue.length < 5 )
    {
        dateElement.style.borderColor = "#ff0000";
    };
    if (dateValue.length == 0 )
    {
        dateElement.style.borderColor = "#000000";
    };
});

/* <input type="submit" id="sub" value="Submit"> */

