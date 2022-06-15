function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();
    
    if (hours < 10) {
        hours = "0" + hours;
    }
    
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    
    let time = hours + ":" + minutes;
    return time;
}

// Gets the first message
function firstBotMessage() {
    let firstMessage = "नमस्ते मेरो नाम जेली हो kylie मायालु "
    document.getElementById("botStarterMessage").innerHTML = `<p class="botText"><img src="../static/img/robot.png"><span> ${firstMessage}</span></p>`;
    
    let time = getTime();
    
    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

function print_user_input(userText) {
    /**
    adds the given userText to the website on user's side
    */
    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';
    $("#chatbox").append(userHtml);
    var chatbox = document.getElementById('chatbox')
    chatbox.scrollTop= chatbox.scrollHeight
}

function print_bot_response(botResponse) {       
    /**
    same as print_user_input but does for bot side
    */
    let botHtml = `<p class="botText"><img src="../static/img/robot.png"><span> ${botResponse}</span></p>`;
    $("#chatbox").append(botHtml);
    var chatbox = document.getElementById('chatbox')
    chatbox.scrollTop= chatbox.scrollHeight
}



var collapser = document.getElementById('collapser');
collapser.addEventListener('click', () => {
    var visiblee = document.getElementById('chatbot')
    var visible = document.getElementById('conversation')
    
    if (visible.style.display != 'none') {
        visible.style.display = 'none'
        visiblee.style.display = 'block'
    } else {
        visible.style.display = 'block'
        visiblee.style.display = 'grid'
    }
})

//Handles the dropdown of the customize-chat-look
var dropdown1 = document.getElementById('dropdown1');
dropdown1.addEventListener('click', () => {
    var dropdown_content1 = document.getElementById('dropdown_content1')
    
    if (dropdown_content1.style.display != 'none') {
        dropdown_content1.style.display = 'none'
    } else {
        dropdown_content1.style.display = 'block'
    }
})


//Handles the dropdown of the customise conversation


var dropdown2 = document.getElementById('dropdown2');
dropdown2.addEventListener('click', () => {
    var dropdown_content2 = document.getElementById('dropdown_content2')
    
    if (dropdown_content2.style.display != 'none') {
        dropdown_content2.style.display = 'none'
    } else {
        dropdown_content2.style.display = 'block'
        
    }
})

//Function for the darkmode mode huhu kati dherai feature halnw baaki chaaaaaaa
var darkmode =document.getElementById('darkmode')

var dark =document.getElementById('dark')
var DBM = document.getElementById('DBM')


dark.addEventListener('click',()=>{
    if (darkmode.style.color!='white'){
        darkmode.style.color= 'white'
        dark.style.backgroundColor='rgba(22, 21, 21, 0.705)'
        DBM.innerHTML= `Dark mode`
        darkmode.style.transform='translateX(-1.2rem) translateY(-0.35rem)'
        dark.style.border= 'none'
        
    }
    else{
        darkmode.style.color='black'
        darkmode.style.transform='translateX(.9rem) translateY(-0.5rem)'
        dark.style.backgroundColor='white'
        dark.style.border= '2px solid rgba(22, 21, 21, 0.705)'
        DBM.innerHTML= `Bright mode`
        
    }
})