var toggleSubmit = function() {
    var len = document.getElementById("nm").value.length;
    var val = document.getElementById("birthdate").value;
    var pattern = /^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])$/;
    var flag = pattern.test(val);
    var submitBtn = document.querySelector("input[type=submit]");

    if (!len || !flag) {
      submitBtn.setAttribute("disabled", "disabled");
    } else {
      submitBtn.removeAttribute("disabled");
    }
  };

document.querySelector("form").addEventListener("input", toggleSubmit, false);