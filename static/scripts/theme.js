//Function for the dark mode
var darkmode = document.getElementById('darkmode');
var dark = document.getElementById('dark');
var dropdown_content1 = document.getElementById('dropdown_content1')
var dropdown_content2 = document.getElementById('dropdown_content2')
var DBM = document.getElementById('DBM');
var themeicon = document.getElementById('themeicon');
var chat_icon5 = document.getElementById('chat-icon5')
var textInput = document.getElementById('textInput')
var botMessage = document.getElementById('botMessage')
var usertextInput = document.getElementById('user-TextInput')
var dark = document.getElementById('dark');
var searchFontIcon = document.getElementById('searchFontIcon')
var close_theme = document.getElementById('close-Theme')
dark.addEventListener('click', () => {
    if (darkmode.style.color != 'white') {
        darkmode.style.color = 'white'
        chatbot.style.background = 'white'
        chatbot.style.color = 'black'
        textInput.style.backgroundColor = '#e0e0e0'
        textInput.style.color = 'black'
        dropdown_content1.classList.add('content')
        dropdown_content1.classList.remove('darktheme')
        dropdown_content2.classList.add('content')
        dropdown_content2.classList.remove('darktheme')
        dropdown_content2.classList.remove('darkredtheme')
        dropdown_content1.classList.remove('darkredtheme')
        dark.style.backgroundColor = 'rgba(22, 21, 21, 0.705)'
        chat_icon5.style.color = 'rgb(34, 33, 33)'
        DBM.innerHTML = `Dark mode`
        DBM.style.backgroundColor = 'rgba(0, 0, 0, 0.685)'
        darkmode.style.transform = 'translateX(-1.2rem) translateY(-0.35rem)'
        dark.style.border = 'none'
        botMessage.style.color = 'black'
        botMessage.style.backgroundColor = '#e0e0e0'
        usertextInput.style.backgroundColor = '#f0f2f5'
        usertextInput.style.color = 'black'

    } else {
        darkmode.style.color = 'black'
        darkmode.style.transform = 'translateX(.9rem) translateY(-0.5rem)'
        dark.style.backgroundColor = 'white'
        chatbot.style.background = 'black'
        dropdown_content1.classList.add('darktheme')
        dropdown_content1.classList.remove('content')
        dropdown_content2.classList.add('darktheme')
        dropdown_content2.classList.remove('content')
        dropdown_content2.classList.remove('darkredtheme')
        dropdown_content1.classList.remove('darkredtheme')

        chatbot.style.color = 'white'
        close_theme.style.color = 'black'
        textInput.style.backgroundColor = 'rgb(84 84 84 / 48%)'
        textInput.style.color = 'white'
        dark.style.border = '2px solid rgba(22, 21, 21, 0.705)'
        DBM.innerHTML = `Bright mode`
        DBM.style.backgroundColor = 'rgba(0, 0, 0, 0.685)'
        chat_icon5.style.color = '#dbdbdb'
        botMessage.style.color = 'white'
        botMessage.style.backgroundColor = 'rgb(84 84 84 / 48%)'
        usertextInput.style.backgroundColor = 'rgb(84 84 84 / 48%)'
        usertextInput.style.color = 'white'
        searchFontIcon.style.color = 'black'
    }
});
//Function for dark-red theme

var red_theme = document.getElementById('dark-red-theme')
red_theme.addEventListener('click', () => {
    chatbot.style.background = 'darkred'
    dropdown_content1.classList.add('darkredtheme')
    dropdown_content1.classList.remove('content')
    dropdown_content2.classList.add('darkredtheme')
    dropdown_content2.classList.remove('content')
    dropdown_content2.classList.remove('dark-red-theme')
    dropdown_content1.classList.remove('dark-red-theme')
    chatbot.style.color = 'white'
    close_theme.style.color = 'darkred'
    dark.style.backgroundColor = 'rgb(190, 19, 19)'
    darkmode.style.color = 'darkred'
    textInput.style.backgroundColor = 'rgb(190 19 19)'
    textInput.style.color = 'white'
    dark.style.border = 'none'
    DBM.style.backgroundColor = 'red'
    chat_icon5.style.color = '#dbdbdb'
    botMessage.style.color = 'white'
    botMessage.style.backgroundColor = 'rgb(190 19 19)'
    usertextInput.style.backgroundColor = 'rgb(84 84 84 / 48%)'
    usertextInput.style.color = 'white'
    searchFontIcon.style.color = 'black'

})