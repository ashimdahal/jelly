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
    document.getElementById("botStarterMessage").innerHTML = `<p class="botText search"><img src="../static/img/robot.png"><span id="botMessage"> ${firstMessage}</span></p>`;

    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

function print_user_input(userText) {
    /**
    adds the given userText to the website on user's side
    */
    let userHtml = '<p class="userText"><span class="search">' + userText + '</span></p>';
    $("#chatbox").append(userHtml);
    var chatbox = document.getElementById('chatbox')
    chatbox.scrollTop = chatbox.scrollHeight
}

function print_bot_response(botResponse) {
    /**
    same as print_user_input but does for bot side
    */
    let botHtml = `<p class="botText search"><img src="../static/img/robot.png"><span  id="botMessage"> ${botResponse}</span></p>`;
    $("#chatbox").append(botHtml);
    var chatbox = document.getElementById('chatbox')
    chatbox.scrollTop = chatbox.scrollHeight
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
var dropdown_content1 = document.getElementById('dropdown_content1')
var dropdown1 = document.getElementById('dropdown1');
dropdown1.addEventListener('click', () => {
    var angle_down1 = document.getElementById('angle_down1')
    var angle_up1 = document.getElementById('angle_up1')


    if (dropdown_content1.style.display != 'none') {
        dropdown_content1.style.display = 'none'
        angle_up1.style.display = 'none'
        angle_down1.style.display = 'block'

    } else {
        dropdown_content1.style.display = 'block'
        angle_up1.style.display = 'block'
        angle_down1.style.display = 'none'
    }
})


//Handles the dropdown of the customise conversation


var dropdown2 = document.getElementById('dropdown2');
var dropdown_content2 = document.getElementById('dropdown_content2')
dropdown2.addEventListener('click', () => {
    var angle_down2 = document.getElementById('angle_down1')
    var angle_up2 = document.getElementById('angle_up1')

    if (dropdown_content2.style.display != 'none') {
        dropdown_content2.style.display = 'none'
        angle_up2.style.display = 'none'
        angle_down2.style.display = 'block'

    } else {
        dropdown_content2.style.display = 'block'
        angle_up2.style.display = 'block'
        angle_down2.style.display = 'none'

    }
})


//Function for the close button

//...............
var robot1 = document.getElementById('robot1');
var background = document.getElementById('background')
var chatbot = document.getElementById('chatbot')
var close = document.getElementById('close')
var visible = document.getElementById('conversation')

close.addEventListener('click', () => {
    chatbot.style.animation = 'collapse 1.5s'
    setTimeout(() => {
        chatbot.style.display = 'none';
        background.style.display = 'flex'
        background.style.animation = 'rotatee 1.5s'
    }, 1500)

})
robot1.addEventListener('click', () => {
    background.style.animation = 'collapse 1.5s'
    setTimeout(() => {
        background.style.display = 'none';
        chatbot.style.display = 'grid'
        visible.style.display = 'block'
        chatbot.style.animation = 'rotatee 1.5s'
    }, 1500)
})

//function for the delete conversation
var deleteConversation = document.getElementById('deleteConversation')

deleteConversation.addEventListener('click', () => {
    var chat_timestamp = document.getElementById('chat-timestamp')
    var botText = document.querySelectorAll('.botText');
    var userText = document.querySelectorAll('.userText');
    userText.forEach(user => {
        user.remove();
    });
    botText.forEach(bot => {
        bot.remove();
    });
    chat_timestamp.remove();

})

//function of search  button 
const user_TextInput= document.querySelector("#user-TextInput");
var searchConversation = document.getElementById('searchConversation');
var searchbar = document.getElementById('searchbar');
searchConversation.addEventListener('click', ()=>{
    if (searchbar.style.display!='none'){
        searchbar.style.display='none'
        searchConversation.style.transform='scale(1)'

        user_TextInput.value=""
        
    }
    else{
        searchbar.style.display='block'
            searchConversation.style.transform='scale(1.05)'
        }
       

        
    
})
//function for the close button of the search content
document.getElementById('closee').addEventListener('click', ()=>{
    searchbar.style.display='none'
    searchConversation.style.transform='scale(1)'
    user_TextInput.value=""
   
})

//function to search the content of the chat 

document.getElementById('user-TextInput').addEventListener('input', searchContent);

function searchContent()
{
    const user_TextInput= document.querySelector("#user-TextInput");
    const filter = user_TextInput.value.toLowerCase();

    var content =document.querySelectorAll('.search');
    content.forEach(item => {
        let text = item.textContent
        if (text.toLowerCase().includes(filter.toLowerCase())){
            item.style.display='';

        }
        else{
            item.style.display='none'
        }
        
    });
}

//function for the close button of theme-container
var closeThemeContainer= document.getElementById('closeThemeContainer')
var outerTheme_Container= document.getElementById('outerTheme-Container')

closeThemeContainer.addEventListener('click', ()=>{
    outerTheme_Container.style.display='none'
    changeThemeButton.style.transform='scale(1)'
})
//function for the changeThemeButton 
var changeThemeButton = document.getElementById('changeThemeButton')
changeThemeButton.addEventListener('click', ()=>{
    
    if(outerTheme_Container.style.display!='block'){
        outerTheme_Container.style.display='block'
        changeThemeButton.style.transform='scale(1.05)'

    }
   else{
    outerTheme_Container.style.display='none'
    changeThemeButton.style.transform='scale(1)'
   }
});