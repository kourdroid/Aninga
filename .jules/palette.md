## 2026-07-31 - CustomTkinter Keyboard Accessibility Gap
**Learning:** CustomTkinter's CTkButton and CTkRadioButton components do not natively execute their commands when a keyboard user presses <space> or <Return>, unlike standard web or OS components, which breaks full keyboard accessibility.
**Action:** Always manually bind <space> and <Return> keys to invoke the widget's action (via _command() for buttons or invoke() for radio buttons), ensuring to defensively check that the button is not disabled (w.cget('state') != 'disabled') and the command exists.
