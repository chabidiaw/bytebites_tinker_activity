# Reflection

## Bug Reproduction Log

### Issue

When I first tried to push my project to GitHub, I received the error:

```
fatal: No configured push destination.
```

### Cause

I had initialized my local Git repository and committed my files, but I had not connected the repository to a remote GitHub repository.

### Solution

I created a repository on GitHub, added it as the remote origin, and then pushed my code using:

```bash
git remote add origin https://github.com/chabidiaw/bytebites_tinker_activity.git
git branch -M main
git push -u origin main
```

### Result

My local repository successfully synchronized with GitHub, and future pushes can be completed with `git push`.

---

## AI Collaboration Reflection

### How I Used AI

I used AI as a design partner throughout the project. I asked for help generating an initial UML diagram, creating behavioral instructions for my reference file, planning class structures, and understanding Git errors.

### What Was Helpful

AI was especially useful for:

- Turning the feature request into candidate classes
- Explaining UML relationships
- Suggesting scaffold structures for Python classes
- Helping diagnose Git configuration issues

### What I Had to Verify

I learned that I could not accept every AI suggestion automatically. I needed to compare generated UML diagrams and code against the project specification and remove unnecessary complexity when suggestions went beyond the requirements.

### What I Learned

This project helped me practice breaking a vague feature request into classes, designing a simple object-oriented system, using Git and GitHub workflows, and treating AI as a collaborator whose output still requires human review and verification.
