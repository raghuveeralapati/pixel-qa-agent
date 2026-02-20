# Contributing to Pixel QA Agent 🚀

Thank you for your interest in contributing to **Pixel QA Agent**!
We welcome contributions from developers, QA engineers, designers, and AI enthusiasts.

⚠️ **Important:**
All contributions must go through Pull Requests. Direct pushes or commits to the `main` branch are restricted.

---

## 📌 Table of Contents

* Code of Conduct
* Getting Started
* Project Setup
* Branching Strategy
* Development Guidelines
* Commit Message Convention
* Testing Guidelines
* Pull Request Process
* Reporting Issues
* Feature Requests
* Documentation Contributions
* Recognition

---

## 🧭 Code of Conduct

By participating in this project, you agree to:

* Be respectful and inclusive
* Provide constructive feedback
* Collaborate professionally
* Follow open-source best practices

---

## 🚀 Getting Started

### 1. Fork the Repository

Click the **Fork** button on GitHub and clone your fork:

```bash
git clone https://github.com/your-username/pixel-qa-agent.git
cd pixel-qa-agent
```

### 2. Add Upstream Remote

```bash
git remote add upstream https://github.com/raghuveeralapati/pixel-qa-agent.git
```

### 3. Sync with Upstream (Recommended)

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## ⚙️ Project Setup

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate environment:

```bash
# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python app.py
```

(Adjust the entry file if your project uses a different start script.)

---

## 🌿 Branching Strategy (STRICT)

🚫 Direct commits to `main` are NOT allowed.
All changes must be made via feature branches and Pull Requests.

### Create a New Branch

```bash
git checkout -b feature/your-feature-name
```

### Branch Naming Conventions

* `feature/*` → New features
* `dev/*` → Active Developments
* `hotfix/*` → Core updates

Examples:

```bash
feature/add-visual-regression-agent
dev/screenshot-diff-bug
hotfix/update-readme
```

---

## 🧑‍💻 Development Guidelines

### Code Style

* Follow PEP 8 (Python)
* Write clean, modular, and reusable code
* Use meaningful variable and function names
* Add docstrings for public functions and classes
* Avoid hardcoded values
* Keep functions small and testable

### Project Structure

* Keep files organized by module/responsibility
* Do not introduce unnecessary dependencies
* Maintain consistency with the existing architecture

---

## 📝 Commit Message Convention

We follow **Conventional Commits**:

Format:

```
<type>: <short description>
```

Types:

* `feat:` → New feature
* `dev:` → Active developments
* `hotfix:` → Core updates

Examples:

```
feat: add pixel comparison module
dev: resolve screenshot diff timeout
hotfix: update setup instructions
```

---

## 🔍 Testing Guidelines

Before submitting a Pull Request:

* Ensure the project runs locally
* Test new features thoroughly
* Do not break existing functionality
* Add tests if applicable

If the project uses pytest:

```bash
pytest
```

For QA-related contributions:

* Include sample test cases
* Provide screenshots for visual QA features (if applicable)
* Validate edge cases

---

## 📥 Pull Request Process

### Steps to Submit a PR

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit using proper commit messages
5. Push your branch:

```bash
git push origin feature/your-feature-name
```

6. Open a Pull Request to the `main` branch

### Pull Request Checklist

* [ ] Code runs without errors
* [ ] Follows coding standards
* [ ] No direct commits to main
* [ ] Proper branch naming used
* [ ] Documentation updated (if needed)
* [ ] Screenshots added (for UI/visual changes)
* [ ] No sensitive data or secrets committed

---

## 🐛 Reporting Issues

When creating an issue, please include:

* Clear and descriptive title
* Detailed description of the problem
* Steps to reproduce
* Expected vs actual behavior
* Screenshots/logs (if applicable)
* Environment details:

  * OS
  * Python version
  * Browser (if UI-related)
  * Tooling used

Use GitHub Issues for:

* Bugs
* Performance issues
* Unexpected behavior

---

## 💡 Feature Requests

We welcome new ideas and improvements!

Please open an issue with:

* Problem statement
* Proposed solution
* Use case
* Expected impact on Pixel QA Agent

This helps maintainers evaluate and prioritize features effectively.

---

## 📚 Documentation Contributions

You can contribute by:

* Improving README
* Adding usage examples
* Writing tutorials or guides
* Fixing typos and formatting
* Enhancing developer onboarding docs

Documentation PRs are highly appreciated.

---

## 🔒 Security Guidelines

* Do NOT commit API keys or secrets
* Use environment variables for sensitive configs
* Report vulnerabilities privately via issues (or maintainer contact)

---

## ⭐ Recognition

All contributors will be acknowledged in the project’s contributors list.
Your contributions help make Pixel QA Agent better for the community.

Thank you for contributing! 🚀