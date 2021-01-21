function update5(event, tables) {
    val = document.getElementById("big_five").value;
    console.log("here", val);
    document.getElementById('display').innerHTML = tables[val];
}

function updateMathPage(event) {
    val = document.getElementById("math_select").value;
    stats = document.getElementById("stats");
    conversions = document.getElementById("conversions");
    if (val == "stats") {
        stats.style.display = ""
        conversions.style.display = "none"
    } else if (val == "conversions") {
        stats.style.display = "none"
        conversions.style.display = ""
    }
}