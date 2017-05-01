Stripe = {
    setPublishableKey: function (publicKey) {},
    card: {
        createToken: function (cardDetails, callbackFunc) {
            var errorMessage = '';
            if(!cardDetails.number) {
                errorMessage = 'Card number is required';
            } else if(!cardDetails.name) {
                errorMessage = 'Cardholder name is required';
            } else if(!cardDetails.cvc) {
                errorMessage = 'CVC is required';
            }
            if(errorMessage) {
                response = {
                    'error': {
                        'message': errorMessage
                    }
                };
            } else {
                response = {
                    id: '1234-4567-890a-bcde'
                };
            }
            callbackFunc('OK', response);
        }
    },
};
