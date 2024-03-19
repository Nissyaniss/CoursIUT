# Exercice 2

## 2

```java
public class SearchManager extends SearchStrategy {
    searcheStrategy searchStrategy;
    
    public void setSearchStrategy(searchStrategy : SearchStrategy) {
        //Todo
    }

    public List<SearchResult> search() {
        //Todo
    }
}

public interface SearchStrategy {
    public List<SearchResult>();
}

public class SearchDatabase implements SearchStrategy {
    public List<SearchResult> search() {
        //Todo
    }
}

public class SearchOnline implements SearchOnline {
    public List<SearchResult> search() {
        //Todo
    }
}
```

## 3 

```java
public class Client {
    public static void main(String[] args) {
        SearchManager searchManager = new SearchManager();
        SearchOnline searchOnline = new SearchOnline();

        searchManager.setSearchStrategy(searchOnline);
        searchManager.search();

        SearchDatabase searchDatabase = new SearchDatabase();

        searchManager.setSearchStrategy(searchDatabase);
        searchManager.search();
    }
```
