function update5(event, tables) {
    val = document.getElementById("big_five").value;
    console.log("here", val);
    document.getElementById('display').innerHTML = tables[val];
}