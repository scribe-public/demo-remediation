# Add CSRF protection middleware

This PR integrates CSRF protection into the Express application to mitigate CWE-352: Cross-Site Request Forgery (CSRF) by leveraging the `csurf` middleware and `cookie-parser`.

## Changes
- Added `cookie-parser` and `csurf` dependencies to `package.json`.
- Configured CSRF protection in `server.js`:
  - Parsed cookies using `cookie-parser`.
  - Enabled CSRF middleware via `csurf({ cookie: true })`.
  - Set `XSRF-TOKEN` cookie on each request for client usage.
  - Added error handler for invalid CSRF tokens (`EBADCSRFTOKEN`).
- Updated server startup sequence to include CSRF error handling.

## Testing
1. Install new dependencies:
   ```bash
   npm install
   ```
2. Start the server:
   ```bash
   npm start
   ```
3. Verify that a `XSRF-TOKEN` cookie is set when accessing `http://localhost:3000/`.
4. Attempt a POST request without the CSRF token to confirm the server responds with `403 Invalid CSRF token`.

## References
- Semgrep rule: [javascript.express.security.audit.express-check-csurf-middleware-usage](https://semgrep.dev/r/javascript.express.security.audit.express-check-csurf-middleware-usage.express-check-csurf-middleware-usage)
- OWASP CSRF Prevention: https://owasp.org/www-community/attacks/csrf