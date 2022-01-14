# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.
_(maintained by Sujal Singh)_

### RESOURCE LIST

## <br>WAP to generate and display first n fibonacci numbers in a tuple.<br>
```python
"""
WAP to generate and display first n fibonacci numbers in a tuple.
"""
x, n1, n2 = int(input("Enter length of fibonacci series to be displayed: ")), 0, 1

print(f"Fibonacci series till {x}:", n1, n2, sep="\n")
for i in range(x):
    n1, n2 = n2, n1 + n2
    print(n2)

"""
OUTPUT:
Enter length of fibonacci series to be displayed: 10
Fibonacci series till 10:
0
1
1
2
3
5
8
13
21
34
55
89
"""

```


---

#### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Want a missing question to be added
- Need help with a question
- Need help navigating the website
- Website has a bug

#### WANT TO CONTRIBUTE RESOURCES?

_Fork this [repository](https://github.com/sujaldev/school), make changes, create a pull request._

---

# Comments

<script src="https://giscus.app/client.js"
        data-repo="sujaldev/school"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzODUzMDMzOTI="
        data-category="Q&A"
        data-category-id="DIC_kwDOFvdDYM4CArKZ"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>