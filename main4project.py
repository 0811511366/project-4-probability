import math

def binomial_pmf(n, k, p=0.5):
    """Calculate binomial probability P(X=k)."""
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

def find_prob():
    n = 10   
    p = 0.5  

    print("We want the probability of observing between 2 and 4 heads out of 10 coin flips.")
    print("Choose the number of heads (k): \n1. Two\n2. Three\n3. Four")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        k = 2
    elif choice == 2:
        k = 3
    elif choice == 3:
        k = 4
    else:
        print("Invalid choice")
        return

    prob = binomial_pmf(n, k, p)
    print(f"Probability of getting exactly {k} heads: {prob:.4f}")

    total_prob = sum(binomial_pmf(n, x, p) for x in range(2, 5))
    print(f"Total probability of getting between 2 and 4 heads: {total_prob:.4f}")

print("Let's calculate probabilities for coin flips")
find_prob()
