## 2024-10-24 - Enable Keyboard Activation for CustomTkinter Widgets
**Learning:** CustomTkinter's `CTkButton` and `CTkRadioButton` widgets do not natively execute their commands when a keyboard user presses `<space>` or `<Return>`. While visual focus states can be added, the widgets remain functionally inaccessible to keyboard navigation without manual key bindings.
**Action:** Always manually bind `<space>` and `<Return>` keys to invoke the widget's action (via `_command()` for buttons or `invoke()` for radio buttons), and include defensive checks to ensure the widget is not disabled.
