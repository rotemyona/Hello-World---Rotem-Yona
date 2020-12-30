function changepic1(x) {
    x.src ="{{ url_for('static', filename='JS/mefunny1.jpg') }}";
}

function changpic2(x) {
    x.src ="{{ url_for('static', filename='JS/meforcactus.jpg') }}";
}
$(".btn").click(function(){
    $(".input, .area").val("");
  });