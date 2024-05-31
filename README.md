
# LeetCode Solutions Repository

Welcome to my LeetCode Solutions repository! This repository contains solutions to various LeetCode problems that I have solved. It serves as a comprehensive archive of my journey through mastering data structures and algorithms.


## Introduction

LeetCode is a powerful platform for improving coding skills through solving challenging problems. This repository is a collection of my solutions to LeetCode problems, organized for easy navigation and reference. It aims to help others who are also preparing for coding interviews or just looking to improve their algorithmic thinking.

## Directory Structure

The repository is structured as follows:

```
.
├── README.md
├── arrays
│   ├── problem1.py
│   ├── problem2.py
│   └── ...
├── linked_lists
│   ├── problem1.py
│   ├── problem2.py
│   └── ...
├── strings
│   ├── problem1.py
│   ├── problem2.py
│   └── ...
├── dynamic_programming
│   ├── problem1.py
│   ├── problem2.py
│   └── ...
└── ...
```

- **arrays/**: Solutions to array-based problems.
- **linked_lists/**: Solutions to linked list problems.
- **strings/**: Solutions to string manipulation problems.
- **dynamic_programming/**: Solutions to dynamic programming problems.
- Additional directories for other categories like graphs, trees, sorting, etc.

## Solutions

Each solution is contained within its own file and is well-documented with comments explaining the approach, time complexity, and any edge cases handled. For instance:

```python
# arrays/problem1.py

class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
```

## Languages Used

- **Python**: Primary language for solving problems.
- Additional languages like Java, C++, etc., can be added as needed.

## Contributing

I welcome contributions from the community! If you have a better solution or an optimization for any problem, feel free to open a pull request. Please ensure your code follows the existing format and is well-commented.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact

If you have any questions or suggestions, feel free to reach out to me at [pereira.austin6602@berkeley.edu](mailto:pereira.austin6602@berkeley.edu). You can also connect with me on [LinkedIn](https://www.linkedin.com/in/austin-pereira).

Happy Coding!
