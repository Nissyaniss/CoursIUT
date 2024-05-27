package wardcardgame.model.material;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class StandardDeck extends Deck {
    private List<Card> cards;

    public StandardDeck() {
        super();
        this.putAllCardsTogether();
    }

    public void putAllCardsTogether() {
        cards = new ArrayList<>();

        for (Suit suit : Suit.values()) {
            for (Rank rank : Rank.values()) {
                cards.add(new Card(rank, suit));
            }
        }
        Collections.shuffle(cards);
    }

    public List<Card> getCards() {
        return cards;
    }
}
