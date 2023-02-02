function func(){
    document.getElementById("DC").style.animationPlayState="running";
    document.getElementById("myAudio").play();

    var speechRecognition = window.webkitSpeechRecognition

    var recognition = new speechRecognition()

    var textbox = $("textbox")

    var instructions = $("instructions")

    var content = ''


    // $.ajax({
    //     url: "{% url 'easy' %}",
    //     type: "GET",
    //     success: successFunc,
    //     error: errorFunc
    // });
    
    // function successFunc(response) {
    //         document.getElementById("p1").innerHTML = response.value;
    //     }
    // function errorFunc() {
    //         alert('error');
    //     }
}
    