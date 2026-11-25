// The site moved to bottobook.yansquared.com. Send the old pages.dev address there (301), keeping path and query.
// Preview deploys (<hash>.bottobook.pages.dev) are left alone.
export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  if (url.hostname === "bottobook.pages.dev") {
    url.hostname = "bottobook.yansquared.com";
    return Response.redirect(url.toString(), 301);
  }
  return next();
}
