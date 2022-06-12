# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.
_(maintained by Sujal Singh)_

## SQL
comment errors and missing syntax down below

#### TO CREATE DATABASE
```sql
CREATE DATABASE "<database name>";
```


#### TO CREATE TABLE
```sql
CREATE TABLE "<table name>" (
        "<column name>" "<data type>" "<constraints>",
        "<column name>" "<data type>" "<constraints>"
);
```


#### TO INSERT VALUES IN TABLE
```sql
INSERT INTO "<table name>" "[columnns, columns]" values(
        "column1", "column2", ...
);
```

#### TO ADD NEW COLUMN
```sql
ALTER TABLE "<table name>"
ADD COLUMN "<column name>" "<data type>";
```


#### TO ADD PRIMARY KEY CONSTRAINT TO EXISTING COLUMN
```sql
ALTER TABLE "<table name>"
ADD PRIMARY KEY ("<column name 1>", "<optional column 2 and more>");
```


#### TO DELETE COLUMN
```sql
ALTER TABLE "<table name>"
DROP COLUMN "<column name>";
```


#### TO DELETE PRIMARY KEY CONSTRAINT
```sql
ALTER TABLE "<table name>"
DROP PRIMARY KEY;
```


#### TO UPDATE VALUES
```sql
UPDATE "<column name>"
SET "<column1>" = "<new value>", "<column2>" = "<new value>", ...
WHERE "<condition>";
```


#### TO DELETE ROWS
```sql
DELETE FROM "<table name>"
WHERE "<condition>";
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
