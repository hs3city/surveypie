# Contributing Guidelines

We are incredibly grateful that you want to contribute to the project!

The project is community-driven and has a set of rules to ensure that development runs smoothly and users get a bug-free program. The rules are short, so please refer to them before you post an issue or write code.

## General Rules
The main rule is: **be respectful to others**. Refer to the Code of Conduct to learn more if you need clarification on what we mean by that.

## Posting Issues and Feature Requests
Have you found a bug? Do you see a space for additional functionality in the package? Then you should go to the `Issues` section! You should know a few points before posting the new issue.

### Bugs
- Check if someone else has reported a bug (use `Filters` above the list of issues). There is a chance that your bug is in the `Closed` section.
- Prepare (1) an error message, (2) code context where your program raised an error, (3) a description of your expectations from the given function, (4) your environment specification, (5) optional - input data, (6) optional - screenshots and code samples.
- Describe a bug using information from the previous point.

### Features
- Describe feature.
- Give links to the bibliography and publications if a requested feature is a statistical method.
- Be prepared that maintainers won't implement the new functionality because of their commitments elsewhere!

## Helping with package development
The package lives as long as contributors are willing to maintain it, so we are thankful you want to put effort into it. To ensure the package has healthy growth, we established ground rules that you **must** apply to your work. 

### Solving issues
- Ask in the issue thread if you can solve it.
- Package admin will create a branch for your work.
- When you solve the issue, run all tests [How should I run tests?]. Create PR **only when all tests pass**. You might need to update the test suite after your corrections; if you need clarification, ask admins what to do in the issue thread.
- Run `black` and `flake8` [How should I lint and validate my code?].
- Push your PR to the `staging` branch.
- Look into your PR's checks. There might be formatting problems. Solve those and commit changes. When all checks are green, we will be ready to go!

### Developing new features
**Caution!** If you are not willing to write tests and docstrings for a feature, it will not be accepted by the maintainers.
- Ideally, ask first if you want to introduce a new feature. Then, you will get additional guidance from the package maintainers, and you will not produce something that might burden other maintainers in the future.
- Every new feature must be well-documented. See [Documenting Features] section in the Developer's Guide.
- Every new feature must have at least one unit or functional test written. See [Writing Tests] section in the Developer's Guide.
- Features derived from scientific literature must be cited in a docstring's `Bibliography` section. See [Citing Others] section in the Developer's Guide.
- *Optional* - write a tutorial about the new feature in a notebook.

### Fixing documentation
We are very grateful for fixing the typos and the documentation style. Please do not use *GenAI* for fixes. If we want it, we will do it. Documentation is a great starting point for the new contributors; automating everything is unnecessary 🤖 🔫

### Writing tutorials
We believe that tutorials are a differentiating factor between standard and outstanding packages! Thus, if you see a space for writing a tutorial - do it! Do it as you wish; there is no required structure.

## Authorship and credit
The author's GitHub handle (and optionally - Name and Surname) is attributed to every feature and tutorial. Only maintainers are mentioned in the papers.