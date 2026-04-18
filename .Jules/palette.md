## 2024-05-15 - Domain-Accurate Placeholders
**Learning:** Using domain-accurate terminology (e.g., "chapters" for Manga instead of "episodes", and "episodes" for Anime instead of "pages") along with concrete inline examples (e.g., "1-10") in input placeholders drastically reduces user confusion and prevents malformed data entry.
**Action:** Always provide examples for expected formats in placeholders, and ensure the terminology aligns exactly with the context of the current view/domain.
## 2024-05-24 - Explicit Initialization of Bound Variables in CustomTkinter
**Learning:** When using CustomTkinter bound variables (like `StringVar`) with UI elements such as radio buttons, failing to provide an initial default `value` results in the UI loading in an empty, unselected visual state. This makes it non-obvious to the user what the default or expected input is, impacting accessibility and intuitive design.
**Action:** Always explicitly initialize bound variables (`ctk.StringVar(value='default_option')`) so that the UI correctly reflects a selected state upon loading, ensuring a clear and immediate understanding of the available options.
