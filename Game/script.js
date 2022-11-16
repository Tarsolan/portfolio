document.querySelector("#get-new-deck").addEventListener("click", newDeck);
container = document.querySelector("#main");
var card_pic_here = document.querySelector("#card");
{
  high_score = 0;
}
globalThis;

function newDeck() {
  // Starts the game from its default values - every variable (except the high score) is reset at the global level
  if (counter > high_score) {
    high_score = counter;
    document.querySelector("#high-score").innerHTML = ` ${high_score}`;
  }

  {
    counter = 0;
    card_number_1 = "";
    card_pic_1 = "";
    card_pic_2 = "";
    card_number_2 = "";
    deck_id = "new";
    guess_side = "right";
  }
  globalThis;

  document.querySelector("#counter").innerHTML = ` ${counter}`;

  fetch(`https://deckofcardsapi.com/api/deck/new/draw/?count=1`)
    .then(function (res) {
      return res.json();
    })
    .then(function (deck) {
      let card_pic_1 = deck.cards[0].image;
      // Storing the randomly generated deck ID enables us to use the same deck for each subsequent draw
      deck_id = deck.deck_id;
      card_number_1 = cardValue(deck.cards[0].value);
      console.log(card_number_1);
      card_pic_here.innerHTML = `<div id="card-1" class="card-pic"><img src=${card_pic_1}></div>`;
      card_pic_here.innerHTML += `<button id="higher">Higher!</button><div id="next-card"><img src="card-back.png" height="314" width="226"></div><button id="lower">Lower!</button>`;
      createButtons();
    })

    .catch(function (error) {
      console.log(error);
    });
}

function nextCard(guess, id) {
  let card_1 = document.querySelector("#card-1");
  let next_card = document.querySelector("#next-card");
  let xhr = new XMLHttpRequest();

  xhr.open("GET", `https://deckofcardsapi.com/api/deck/${id}/draw/?count=1`);

  xhr.onload = function () {
    if (this.readyState === 4 && this.status === 200) {
      let deck = JSON.parse(this.responseText);
      let card_pic_2 = deck.cards[0].image;
      card_number_2 = cardValue(deck.cards[0].value);
      console.log(card_number_2);

      // This will take the second card and make it the first card, and return the new space to it's blank form.
      // IF THE UNKNOWN CARD IS ON THE RIGHT
      setTimeout(function () {
        if (guess == "high" && card_number_1 < card_number_2) {
          showAlert("Guess was correct!", "correct");
        } else if (guess === "low" && card_number_1 > card_number_2) {
          showAlert("Guess was correct!", "correct");
        } else if (card_number_1 === card_number_2) {
          showAlert("It's a tie! I guess you win.", "tie");
        } else {
          showAlert(`Guess was wrong. Game will now reset.`, "wrong");
        }
      }, 1000);

      if (guess_side == "right") {
        next_card.innerHTML = `<img src=${card_pic_2}>`;
        // This sets up the variables so that the program guesses for the opposite side next time
        setTimeout(function () {
          card_1.innerHTML = `<img src="card-back.png" height="314" width="226">`;
          card_number_1 = card_number_2;
          guess_side = "left";
        }, 1000);
        // IF THE UNKNOWN CARD IS ON THE LEFT
      } else {
        card_1.innerHTML = `<img src=${card_pic_2}>`;
        // This sets up the variables so that the program guesses for the opposite side next time
        setTimeout(function () {
          next_card.innerHTML = `<img src="card-back.png" height="314" width="226">`;
          card_number_1 = card_number_2;
          guess_side = "right";
        }, 1000);
      }
    }
  };
  xhr.send();
}

function cardValue(card) {
  switch (card) {
    case "JACK":
      card_number = 11;
      break;
    case "QUEEN":
      card_number = 12;
      break;
    case "KING":
      card_number = 13;
      break;
    case "ACE":
      card_number = 14;
      break;
    default:
      card_number = +card;
  }
  return card_number;
}

function createButtons() {
  // I'm not actually sure this is necessary, but I needed the buttons to be selected AFTER they were created, so I made a function for it
  let higher = document.querySelector("#higher");
  let lower = document.querySelector("#lower");

  higher.addEventListener("click", function () {
    nextCard("high", deck_id);
  });
  lower.addEventListener("click", function () {
    nextCard("low", deck_id);
  });
}

function showAlert(message, className) {
  // Taken from class - it creates a div and appends it to the bottom of the page, then deletes it a couple seconds later
  var div = document.createElement("div");
  div.className = className;
  div.innerHTML = message;
  div.id = "result";
  container.appendChild(div);

  setTimeout(function () {
    if (className === "wrong") {
      newDeck();
    } else {
      counter++;
      document.querySelector("#counter").innerHTML = ` ${counter}`;
    }
    document.querySelector("#result").remove();
  }, 2000);
}
