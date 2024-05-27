package wardcardgame.model.material;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Objects;

public class Deck {
    private List<Card> cards;

    public Deck() {
        this.cards = new ArrayList<>();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Deck deck = (Deck) o;
        return Objects.equals(cards, deck.cards);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(cards);
    }

    public Boolean isEmpty() {
        return cards.isEmpty();
    }

    public Boolean put(Card... otherCards) {
        if (otherCards.length == 0)
            return false;
        for (Card card : otherCards) {
            if (card != null)
                this.cards.add(card);
        }
        return true;
    }

    public Boolean put(Collection<Card> otherCards) {
        cards.addAll(otherCards);
        if (otherCards.size() == 0)
            return false;
        return true;
    }

    public Integer remainingCards() {
        return cards.size();
    }

    public Collection<Card> cards() {
        return cards;
    }

    public void clear() {
        cards.clear();
    }

    public Card draw() {
        if (cards.size() == 0)
            return null;
        return cards.remove(0);
    }
}
