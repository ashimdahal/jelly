function getBotResponse(input) {
    // Simple responses
    if (input == "hello") {
        return "नमस्ते";
    } else if (input == "goodbye") {
        return "पछि कुरा गर्छु ।धन्यवाद !";
    } else if (input == "I love you") {
        return "म तिमीलाई धेरै माया गर्छू!";
    } else if (input == "Hey chatbot") {
        return "नमस्ते";
    } else if (input == "This is my heart for you") {
        return "तपाईंको हृदयको लागि धन्यवाद! म यसलाई यो पृथ्वीको अन्त्य सम्म माया गर्नेछु";
    } else {
        return "अरू केही सोध्ने प्रयास गर्नुहोस्! म पूर्ण रूपमा प्रशिक्षित छैन!";
    }
}