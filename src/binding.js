import { EditorView, basicSetup } from "codemirror"
import { EditorState } from "@codemirror/state"
import { sql } from "@codemirror/lang-sql"

class CodeMirrorInputBinding extends Shiny.InputBinding {
    initialize(el) {
      this.editor = null;
    }

    find(scope) {
      return $(scope).find(".codemirror-input");
    }
  
    getValue(el) {
      if (this.editor === null) return "";
      console.log(this.editor.state.doc.toString());
      return this.editor.state.doc.toString();
    }

    subscribe(el, callback) {
      const state = EditorState.create({
        extensions: [
            basicSetup, 
            sql(),
            EditorView.updateListener.of((update) => {
              if (update.docChanged) {
                console.log("TEST");
                callback();
              }
            })
        ]
      });

      this.editor = new EditorView({
          state: state,
          parent: el
      })
    }
  }
  
  Shiny.inputBindings.register(new CodeMirrorInputBinding(), "codemirror-input");




