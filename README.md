# Conan starter project

A modern, production-ready starter template for C++ projects, designed to scale from small experiments to long-lived, professional codebases.

This repository focuses on **correctness, reproducibility, and maintainability** by combining modern C++ practices with a carefully curated toolchain.

---

## Why this template exists

Starting a C++ project often means repeatedly solving the same non-trivial problems:

* setting up CMake correctly
* handling dependencies across platforms
* enforcing code quality consistently
* making CI reliable and reproducible

This template solves these problems once, in a clean and opinionated way, so teams can focus on writing C++ instead of fighting infrastructure.

---

## Goals and Features

### Build & Tooling

1. **Modern CMake ecosystem**
   Uses state-of-the-art CMake together with CTest and CPack, enabling straightforward build configuration, testing, and packaging.

2. **Modern C++ support**
   CMake is configured to expose modern C++ standards and features in a clear and idiomatic way.

3. **Configurable build presets**
   CMake Presets provide standardized build configurations (Debug, Release, Coverage, Sanitizers, etc.).

4. **Cross-platform compatibility**
   Designed to compile and run across major platforms and toolchains (GCC, Clang, MSVC).

5. **Strict compiler warnings**
   Comprehensive warnings are enabled and treated as errors to prevent technical debt.

---

### Reproducibility & Environment

6. **Reproducible development environment**
   Universal Docker image(s) ensure consistent builds and tooling across machines and CI.

7. **Dependency management with Conan**
   External dependencies are managed via Conan and seamlessly integrated with CMake.

---

### Quality & Analysis

8. **Static analysis**
   Integrates tools such as `cppcheck` to detect common issues early.

9. **Extended linting (optional)**
   Optional support for `clang-tidy` to enforce modern C++ best practices.

10. **Formatting and style enforcement**
    Code formatting via `clang-format` with a documented and enforced style.

11. **Clean code enforcement**
    Quality gates and conventions aligned with clean code principles.

12. **Quality gates with SonarQube**
    SonarQube integration to track bugs, vulnerabilities, code smells, and technical debt.

---

### Testing & Verification

13. **Automated testing**
    Unit tests are integrated via CTest and run automatically in CI.

14. **Code coverage reporting**
    Coverage generation and reporting using `gcov` / `lcov`.

---

### CI / CD

15. **Continuous Integration (CI)**
    CI pipelines (GitHub Actions) automate builds, tests, and quality checks.

16. **CI visibility**
    CI status badges are displayed in the README for immediate feedback on project health.

17. **Packaging and artifacts**
    Build artifacts and packages can be generated automatically via CPack.

---

### Documentation & Structure

18. **Clear and scalable project structure**
    Enforces a well-defined directory layout with clear separation of responsibilities.

19. **Documentation tooling (optional)**
    Optional API documentation generation (e.g. Doxygen), with CI integration.

20. **Template extensibility**
    Easily adaptable for libraries, executables, or mixed projects without major restructuring.

21. **Versioning strategy**
    Clear conventions for project versioning and release management.

---

## Suggested Project Structure

```text
.
├── cmake/              # CMake modules and helper scripts
├── conan/              # Conan profiles and configuration
├── docker/             # Dockerfiles for development and CI
├── docs/               # Project and architecture documentation
├── include/            # Public headers
├── src/                # Source files
├── tests/              # Unit and integration tests
├── tools/              # Tooling configuration (clang-format, clang-tidy, etc.)
├── .github/            # CI workflows and templates
├── CMakeLists.txt      # Root CMake configuration
├── CMakePresets.json   # Standardized build presets
└── README.md
```

---

## Philosophy

This template is intentionally opinionated.

* Prefer **explicit configuration** over magic
* Prefer **compile-time guarantees** over runtime surprises
* Prefer **tooling and automation** over manual checks
* Prefer **long-term maintainability** over short-term convenience

You are encouraged to remove or relax constraints if your project requires it — but starting strict makes it easier to stay clean as the codebase grows.

---

## License

Unlicensed.
