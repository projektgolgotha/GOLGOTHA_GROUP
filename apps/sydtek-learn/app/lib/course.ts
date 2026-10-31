export const HRM_PLAYLIST_ID = "PLtS4zDr2sp3S1ptnw-a0Q030421d6jHd0";
export const HRM_PLAYLIST_URL = `https://www.youtube.com/playlist?list=${HRM_PLAYLIST_ID}`;
export type CourseEntry = { position: number; videoId: string; title: string; duration: string; duplicateOf: number | null; url: string };
export type CourseInventory = { available: boolean; entries: CourseEntry[]; uniqueVideoCount: number; capturedAt: string | null };
export function parseCourseInventory(input: unknown): CourseInventory {
  const data = input as { course?: { course_id?: string; source_playlist_id?: string }; source_capture?: { parsed_at_utc?: string }; entries?: Array<{ position?: number; video_id?: string; title?: string; duration_display?: string }> };
  if (!data || data.course?.course_id !== "HRM-101" || data.course.source_playlist_id !== HRM_PLAYLIST_ID || !Array.isArray(data.entries)) throw new Error("Invalid HRM-101 source inventory");
  const seen = new Map<string, number>();
  const entries = data.entries.map((entry, index) => {
    if (entry.position !== index + 1 || !entry.video_id || !/^[A-Za-z0-9_-]{11}$/.test(entry.video_id) || typeof entry.title !== "string" || !entry.title.trim()) throw new Error("Invalid playlist entry");
    const duplicateOf = seen.get(entry.video_id) ?? null;
    if (duplicateOf === null) seen.set(entry.video_id, entry.position);
    return { position: entry.position, videoId: entry.video_id, title: entry.title, duration: entry.duration_display ?? "", duplicateOf, url: `https://www.youtube.com/watch?v=${entry.video_id}&list=${HRM_PLAYLIST_ID}&index=${entry.position}` };
  });
  return { available: true, entries, uniqueVideoCount: seen.size, capturedAt: data.source_capture?.parsed_at_utc ?? null };
}
export function playlistEmbedUrl(videoId?: string) {
  if (videoId !== undefined && !/^[A-Za-z0-9_-]{11}$/.test(videoId)) throw new Error("Invalid video identifier");
  return videoId ? `https://www.youtube-nocookie.com/embed/${videoId}?list=${HRM_PLAYLIST_ID}` : `https://www.youtube-nocookie.com/embed/videoseries?list=${HRM_PLAYLIST_ID}`;
}
