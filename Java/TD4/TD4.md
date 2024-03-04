# Exercice 1

> Voir TD4.mdj

# Exercice 2

```console
I'm a Queen, any questions?
I'm a HonyBee!
I'm a worker, I work all day!
I'm a worker, I work all day!
I'm a HonyBee!
I'm a drone, I'm going to date our Queen!
------------------
I believe, I can fly.
I believe, I can fly.
I believe, I can fly.
I believe, I can fly.
I believe, I can fly.
I believe, I can fly.
```

# Exercice 3

## A

```console
I'm a Queen, any questions?
I'm a HonyBee!
I'm a HonyBee! I'm a worker, I work all day!
I'm a HonyBee! I'm a worker, I work all day!
I'm a HonyBee!
I'm a drone, I'm going to date our Queen!
```

## B

> ```java
> super.doYourWork();
> ```
> N'existe pas pour `HoneyBee`.

# Exercice 4

## A

> L'attribut `name` doit être ajouté a la classe `HoneyBee`.

## B

```java
public class HoneyBee {
    protected final String name;

    public HoneyBee(String name) {
        this.name = name;
    }

    public String doYourJob() {
        return this.name + " I'm a HoneyBee!";
    }
    ...
}

public class Queen Extends HoneyBee {
    public Queen(String name) {
        super(name);
    }
    ...
}

public class Worker extends HoneyBee {
    public Worker(String name) {
        super(name);
    }
}

public class Drone extends HoneyBee {
    public Drone(String name) {
        super(name);
    }
}
```

# Exercice 5

## A

> Abeille, Reine, Ouvrière, Faux-Bourdon.

## B

> Mettre la classe `HoneyBee` en `abstract`.

## C

```java
public class Main {
    public static void main(String[] args) {
        HoneyBee honeyBee = new Queen("Mellifera");
        HoneyBee firstWorker = new Worker("Maya");
        HoneyBee secondWorker = new Worker("Marguerite");
        HoneyBee thirdWorker = new Worker("Propolis");
        HoneyBee firstDrone = new Drone("Willy");
        HoneyBee secondDrone = new Drone("Didier");
    }
}
```

## D

> Oui il y en a sur toute celle qui `extend HoneyBee` sur la méthode `doYourWork()`.

## E

> `@Override`

# Exercice 6

## A

> ```java
> public class Main {
>     public static void main(String[] args) {
>         HoneyBee honeyBees[] = {
>             new Queen("Mellifera"),
>             new Worker("Maya"),
>             new Worker("Marguerite"),
>             new Worker("Propolis"),
>             new Drone("Willy"),
>             new Drone("Didier"),
>         };
>     }
> }
> ```

## B

```java
public class Main {
    public static void main(String[] args) {
        HoneyBee honeyBees[] = {
            new Queen("Mellifera"),
            new Worker("Maya"),
            new Worker("Marguerite"),
            new Worker("Propolis"),
            new Drone("Willy"),
            new Drone("Didier"),
        };
        for (HoneyBee honeyBee : honeyBees) {
            System.out.println(honeyBee.doYourJob());
            System.out.println(honeyBee.fly());
            System.out.println("--------------------------------------------");
        }
    }
}
```

## C

```java
public class Main {
    public static void main(String[] args) {
        int numberBee = 0;
        int numberQueen = 0;
        int numberWorker = 0;
        int numberDrone = 0;

        HoneyBee honeyBees[] = {
            new Queen("Mellifera"),
            new Worker("Maya"),
            new Worker("Marguerite"),
            new Worker("Propolis"),
            new Drone("Willy"),
            new Drone("Didier"),
        };

        for (HoneyBee honeyBee : honeyBees) {
            System.out.println(honeyBee.doYourJob());
            System.out.println(honeyBee.fly());
            System.out.println("--------------------------------------------");
        }

        for (HoneyBee honeyBee : honeyBees) {
            if (honeyBee instanceof Queen) {
                numberQueen++;
            }
            if (honeyBee instanceof Worker) {
                numberWorker++;
            }
            if (honeyBee instanceof Drone) {
                numberDrone++;
            }
            numberBee++;
        }

        System.out.println("My colony has " + numberBee + " honeybees");
        System.out.println(" -> " + numberQueen + " queen(s)");
        System.out.println(" -> " + numberWorker + " worker(s)");
        System.out.println(" -> " + numberDrone + " drone(s)");
    }
}
```
