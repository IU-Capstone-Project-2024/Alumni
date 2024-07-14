function MultiselectDropdown(options) {
  var config = {
      search: true,
      height: '15rem',
      placeholder: 'Tags: any',
      txtSelected: 'selected',
      txtAll: 'All',
      txtRemove: 'Remove tag',
      txtSearch: 'Start typing',
      ...options
  };

  function CreateElement(tag, attrs) {
      var element = document.createElement(tag);
      if (attrs !== undefined) Object.keys(attrs).forEach(key => {
          if (key === 'class') {
              Array.isArray(attrs[key]) ? attrs[key].forEach(cls => cls !== '' ? element.classList.add(cls) : 0) : (attrs[key] !== '' ? element.classList.add(attrs[key]) : 0)
          } else if (key === 'style') {
              Object.keys(attrs[key]).forEach(style_key => {
                  element.style[style_key] = attrs[key][style_key];
              });
          } else if (key === 'text') { attrs[key] === '' ? element.innerHTML = '&nbsp;' : element.innerText = attrs[key] }
          else element[key] = attrs[key];
      });
      return element;
  }

  document.querySelectorAll("select[multiple]").forEach((el, key) => {

      var div = CreateElement('div', { class: 'multiselect-dropdown', style: { width: config.style?.width ?? el.clientWidth + 'px', padding: config.style?.padding ?? '' } });
      el.style.display = 'none';
      el.parentNode.insertBefore(div, el.nextSibling);
      var listWrap = CreateElement('div', { class: 'multiselect-dropdown-list-wrapper' });
      var list = CreateElement('div', { class: 'multiselect-dropdown-list', style: { height: config.height } });
      var search = CreateElement('input', { class: ['multiselect-dropdown-search'].concat([config.searchInput?.class ?? 'form-control']), style: { width: '100%', display: el.attributes['multiselect-search']?.value === 'true' ? 'block' : 'none' }, placeholder: config.txtSearch });
      listWrap.appendChild(search);
      div.appendChild(listWrap);
      listWrap.appendChild(list);

      el.loadOptions = () => {
          list.innerHTML = '';

          if (el.attributes['multiselect-select-all']?.value === 'true') {
              var op = CreateElement('div', { class: 'multiselect-dropdown-all-selector' })
              var ic = CreateElement('input', { type: 'checkbox' });
              op.appendChild(ic);
              op.appendChild(CreateElement('label', { text: config.txtAll }));

              op.addEventListener('click', () => {
                  op.classList.toggle('checked');
                  op.querySelector("input").checked = !op.querySelector("input").checked;

                  var ch = op.querySelector("input").checked;
                  list.querySelectorAll(":scope > div:not(.multiselect-dropdown-all-selector)")
                      .forEach(i => { if (i.style.display !== 'none') { i.querySelector("input").checked = ch; i.optEl.selected = ch } });

                  el.dispatchEvent(new Event('change'));
              });
              ic.addEventListener('click', (ev) => {
                  ic.checked = !ic.checked;
              });

              list.appendChild(op);
          }

          Array.from(el.options).map(o => {
              var op = CreateElement('div', { class: o.selected ? 'checked' : '', optEl: o })
              var ic = CreateElement('input', { type: 'checkbox', checked: o.selected });
              op.appendChild(ic);
              op.appendChild(CreateElement('label', { text: o.text }));

              op.addEventListener('click', () => {
                  op.classList.toggle('checked');
                  op.querySelector("input").checked = !op.querySelector("input").checked;
                  op.optEl.selected = !!!op.optEl.selected;
                  el.dispatchEvent(new Event('change'));
              });
              ic.addEventListener('click', (ev) => {
                  ic.checked = !ic.checked;
              });
              o.listitemEl = op;
              list.appendChild(op);
          });
          div.listEl = listWrap;

          div.refresh = () => {
              div.querySelectorAll('span.optext, span.placeholder').forEach(t => div.removeChild(t));
              var sels = Array.from(el.selectedOptions);

              var containerWidth = div.clientWidth;
              var totalWidth = 0;
              var exceed = false;

              if (sels.length > 0) {
                  sels.forEach((x, i) => {
                      var c = CreateElement('span', { class: 'optext', text: x.text, srcOption: x });
                      if ((el.attributes['multiselect-hide-x']?.value !== 'true')) {
                          c.appendChild(CreateElement('span', { class: 'optdel', text: '🗙', title: config.txtRemove, onclick: (ev) => { c.srcOption.listitemEl.dispatchEvent(new Event('click')); div.refresh(); ev.stopPropagation(); } }));
                      }

                      div.appendChild(c);
                      totalWidth += c.offsetWidth;

                      if (totalWidth >= containerWidth) {
                          exceed = true;
                      }

                      if (exceed) {
                          div.removeChild(c);
                          div.querySelectorAll('span.optext').forEach(optext => optext.remove());
                      }
                  });

                  if (exceed) {
                      div.appendChild(CreateElement('span', { class: ['optext', 'maxselected'], text: sels.length + ' ' + config.txtSelected }));
                  }
              } else {
                  div.appendChild(CreateElement('span', { class: 'placeholder', text: el.attributes['placeholder']?.value ?? config.placeholder }));
              }
          };

          div.refresh();
      }
      el.loadOptions();

      search.addEventListener('input', () => {
          list.querySelectorAll(":scope div:not(.multiselect-dropdown-all-selector)").forEach(d => {
              var txt = d.querySelector("label").innerText.toUpperCase();
              d.style.display = txt.includes(search.value.toUpperCase()) ? 'block' : 'none';
          });
      });

      div.addEventListener('click', () => {
          div.listEl.style.display = 'block';
          search.focus();
          search.select();
      });

      document.addEventListener('click', function(event) {
          if (!div.contains(event.target)) {
              listWrap.style.display = 'none';
              div.refresh();
          }
      });
  });
}

function applyFilters(event) {
    const form = document.getElementById("filter-form");
    const formData = new FormData(form);

    const country = formData.get("country");
    const city = formData.get("city");
    const tagsSelect = document.getElementById("tags");
    const selectedTags = [];
    for (let option of tagsSelect.options) {
        if (option.selected) {
            selectedTags.push(option.value);
        }
    }

    const params = new URLSearchParams();
    params.append("country", country);
    params.append("city", city);
    selectedTags.forEach(tag => params.append("tags", tag));

    const url = `filter_events/?${params.toString()}`;

    fetch(url, {
        method: 'GET',
    })
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, 'text/html');
        document.querySelector('.grid-container').innerHTML = doc.querySelector('.grid-container').innerHTML;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function aiRecommendation(event) {
    document.querySelectorAll("select:not([multiple])").forEach(select => {
        select.value = "";
    });

    const tagsSelect = document.getElementById("tags");
    for (let option of tagsSelect.options) {
        option.selected = false;
    }

    tagsSelect.dispatchEvent(new Event('change'));

    const multiselectDiv = document.querySelector('.multiselect-dropdown');

    if (multiselectDiv) {
        multiselectDiv.querySelectorAll('.multiselect-dropdown-list input[type="checkbox"]').forEach(checkbox => {
            checkbox.checked = false;
        });

        multiselectDiv.querySelectorAll('.multiselect-dropdown-list div.checked').forEach(cb => {
            cb.classList.remove('checked');
            cb.optEl.selected = false;
        });

        multiselectDiv.refresh();
    }
}

function handleSubmit(event) {
    event.preventDefault();
    let action = event.submitter.value;

    (action === 'apply' ? applyFilters : aiRecommendation)(event);
}

window.addEventListener('load', () => {
    MultiselectDropdown(window.MultiselectDropdownOptions);
    const form = document.getElementById("filter-form");
    form.addEventListener("submit", handleSubmit);
});
