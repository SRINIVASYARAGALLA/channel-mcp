---
name: UserPermissionsTabs
description: Guide for creating or updating user-permissions tab components in ChannelWeb2, ensuring consistency and correct data binding.
---

# Purpose

Enable developers to create or update React functional components for user-permissions tabs in ChannelWeb2, using existing data sources and UI conventions.

# Context

- User permissions components are in: `ChannelWeb2/ClientApp/src/components/modules/setup/users/`
- Data comes from `useSelectors()` (returns a `perm` array)
- Each `perm` entry has a `name` (for code lookup) and `title` (for display)
- Use `PlansTab.jsx` as the template for new tabs

# Tab Name Mapping

| Component Name           | perm[].name (code)      | perm[].title (display)         |
|-------------------------|-------------------------|-------------------------------|
| PlansTab                | "Plans"                 | Plans                         |
| ActionsTab              | "Actions"               | Actions                       |
| ModulesTab              | "Modules"               | Modules                       |
| TabsTab                 | "Tabs"                  | Tabs                          |
| ScenariosTab            | "Scenarios"             | Scenarios                     |
| ViewsTab                | "Views"                 | Views                         |
| ReportDefinitionsTab    | "Report Definitions"    | Report Definitions            |
| WhatIdDefinitionsTab    | "What Id Definitions"   | What Id Definitions           |
| DashboardTab            | "Dashboard"             | Dashboard                     |

# Implementation Checklist

- [ ] Confirm which tab/component to create or update
    - If unclear, ask:  
      _"Which permissions tab do you want to create/update? Choose one: Plans, Actions, Modules, Tabs, Scenarios, Views, Report Definitions, What Id Definitions, Dashboard."_
    - If `fackData.json` is available, use `perm[].title` for choices
- [ ] Use `PlansTab.jsx` as the starting template
- [ ] Fetch permissions using the selector hook (`useSelectors`)
- [ ] Select row data using:  
    ```js
    const permName = perm?.find(p => p.title == selectedTitle)?.name ?? selectedTitle;
    const rowData = perm?.find(i => i.name == permName);
    ```
- [ ] Keep DataGrid structure and columns consistent with `PlansTab.jsx`
- [ ] Do not add new UX, columns, or actions unless requested
- [ ] Export and wire the new tab into the tabs container/navigation

# Reference

- Sample data: `src/components/modules/setup/users/data/fackData.json`
- Data selectors: `useQueryModule.jsx`, `useSelectors.jsx`

# Conventions

- Use React functional components and hooks
- Follow the pattern: `perm?.find(i => i.name == "...")`
- Match file naming, exports, and import style to the existing codebase

# Custom Instructions

- 2026-02-25 03:15: Updated ScenariosTab rowHeaderValue: now uses the ps-3 class if parentType is not 2, and renders the title in bold if parentType is 2. (Status: applied)
- 2026-02-25 23:51: Updated ViewsTab rowHeaderValue: now renders the title in bold if parentType is 3, otherwise adds the ps-3 class. (Status: applied)
