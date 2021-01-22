function update5(event, tables) {
    val = document.getElementById("big_five").value;
    console.log("here", val);
    document.getElementById('display').innerHTML = tables[val];
}

function updateMathPage(event) {
    val = document.getElementById("math_select").value;
    big_o = document.getElementById("big_o");
    stats = document.getElementById("stats");
    units = document.getElementById("units");
    console.log(val);
    if (val == "big_o") {
        big_o.style.display = "";
        stats.style.display = "none";
        units.style.display = "none";
    } else if (val == "stats") {
        big_o.style.display = "none";
        stats.style.display = "";
        units.style.display = "none";
    } else if (val == "units") {
        big_o.style.display = "none";
        stats.style.display = "none";
        units.style.display = "";
    }
}