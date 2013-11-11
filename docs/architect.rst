Architect
=========
There are two ways to update or save publishing status, title, slug or other
entry fields. The end user should be use customized form (named ZenModeForm) to
add or update an article information. But if you want to update entry model
object directly, metadata will be update for object fields::

  form --> model
  - update fields for content metadata

  model --> form
  - update metadata for fields

Some metadata elements should be required in content field:

- title
- slug

Optional elements:

- tags
- is_published (default: false)
- image
